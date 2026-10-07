package com.job.service.impl;

import cn.hutool.core.bean.BeanUtil;
import cn.hutool.core.collection.CollectionUtil;
import cn.hutool.core.util.RandomUtil;
import cn.hutool.crypto.digest.DigestUtil;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.job.constant.MessageConstants;
import com.job.constant.RedisConstants;
import com.job.dto.UserLoginDTO;
import com.job.dto.UserRegisterDTO;
import com.job.dto.VerifyCaptchaDTO;
import com.job.entity.User;
import com.job.mapper.UserMapper;
import com.job.service.UserService;
import com.job.util.*;
import lombok.extern.slf4j.Slf4j;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.List;
import java.util.concurrent.TimeUnit;

@Service
@Slf4j
public class UserServiceImpl implements UserService {
    @Resource
    private StringRedisTemplate stringRedisTemplate;

    @Resource
    private EmailUtil emailUtil;

    @Resource
    private UserMapper userMapper;

    @Resource
    private JwtUtil jwtUtil;

    @Override
    public Result sendCaptcha(String username, String email) {
        if (RegexUtil.isUsernameInvalid(username)) {
            return Result.fail(MessageConstants.USERNAME_FORMAT_ERROR);
        }
        //校验邮箱是否合法
        if (RegexUtil.isEmailInvalid(email)) {
            // 如果不符合，返回错误信息
            return Result.fail(HttpStatus.FORBIDDEN.value(), MessageConstants.MAIL_FORMAT_ERROR);
        }

        String identity = username + ":" + email.toLowerCase();
        Boolean permitted = stringRedisTemplate.opsForValue().setIfAbsent(
                RedisConstants.REGISTER_RATE_KEY + identity, "1", 60, TimeUnit.SECONDS);
        if (!Boolean.TRUE.equals(permitted)) {
            return Result.fail(429, "验证码发送过于频繁，请一分钟后重试");
        }
        // 符合，生成验证码
        String code = RandomUtil.randomNumbers(6);
        // 保存验证码到Redis，并设置有效期 5分钟
        stringRedisTemplate.opsForValue().set(RedisConstants.REGISTER_CODE_KEY + identity, code, RedisConstants.REGISTER_CODE_TTL, TimeUnit.MINUTES);

        // 发送验证码
        String subject = "验证码";
        String text = "欢迎注册 Job pilot 平台，您的验证码是：" + code + "，5分钟之内有效";
        boolean success = emailUtil.sendEmail(email, subject, text);
        if (success) {
            log.info("验证码发送成功，username={}", username);
            // 返回
            return Result.success();
        } else {
            stringRedisTemplate.delete(RedisConstants.REGISTER_RATE_KEY + identity);
            stringRedisTemplate.delete(RedisConstants.REGISTER_CODE_KEY + identity);
            return Result.fail(HttpStatus.SERVICE_UNAVAILABLE.value(), MessageConstants.MAIL_SEND_FAIL);
        }
    }

    @Override
    public Result verifyCaptcha(VerifyCaptchaDTO verifyCaptchaDTO) {
        if (verifyCaptchaDTO == null) {
            return Result.fail("验证码请求不能为空");
        }
        String username = verifyCaptchaDTO.getUsername();
        String email = verifyCaptchaDTO.getEmail();
        String captcha = verifyCaptchaDTO.getCaptcha();

        if (RegexUtil.isUsernameInvalid(username) || RegexUtil.isEmailInvalid(email)) {
            return Result.fail("用户名或邮箱格式错误");
        }

        // 校验验证码格式
        if (RegexUtil.isCodeInvalid(captcha)) {
            return Result.fail(MessageConstants.CAPTCHA_FORMAT_ERROR);
        }

        String identity = username + ":" + email.toLowerCase();
        String key = RedisConstants.REGISTER_CODE_KEY + identity;
        String code = stringRedisTemplate.opsForValue().get(key);

        // 验证码已过期
        if (code == null) {
            return Result.fail(MessageConstants.CAPTCHA_TIMEOUT);
        }

        if (captcha.equals(code)) {
            stringRedisTemplate.delete(key);
            stringRedisTemplate.opsForValue().set(
                    RedisConstants.REGISTER_VERIFIED_KEY + identity, "1",
                    RedisConstants.REGISTER_VERIFIED_TTL, TimeUnit.MINUTES);
            return Result.success();
        } else {
            return Result.fail(MessageConstants.CAPTCHA_VERIFY_FAIL);
        }
    }

    @Override
    public Result register(UserRegisterDTO userRegisterDTO) {
        if (userRegisterDTO == null) {
            return Result.fail("注册信息不能为空");
        }
        // 校验格式
        if (RegexUtil.isEmailInvalid(userRegisterDTO.getEmail())) {
            log.info("邮箱格式错误");
            return Result.fail(MessageConstants.MAIL_FORMAT_ERROR);
        }
        if (RegexUtil.isUsernameInvalid(userRegisterDTO.getUsername())) {
            log.info("用户名格式错误");
            return Result.fail(MessageConstants.USERNAME_FORMAT_ERROR);
        }
        if (RegexUtil.isPhoneInvalid(userRegisterDTO.getPhone())) {
            log.info("手机号格式错误");
            return Result.fail(MessageConstants.PHONE_FORMAT_ERROR);
        }
        if (RegexUtil.isPasswordInvalid(userRegisterDTO.getPassword())) {
            log.info("密码格式错误");
            return Result.fail(MessageConstants.PASSWORD_FORMAT_ERROR);
        }
        String verifiedKey = RedisConstants.REGISTER_VERIFIED_KEY
                + userRegisterDTO.getUsername() + ":" + userRegisterDTO.getEmail().toLowerCase();
        if (!"1".equals(stringRedisTemplate.opsForValue().get(verifiedKey))) {
            return Result.fail(MessageConstants.CAPTCHA_VERIFY_FAIL);
        }

        // 构造对象
        User user = new User();
        BeanUtil.copyProperties(userRegisterDTO, user);

        // 加密
        user.setPassword(PasswordUtil.encode(user.getPassword()));

        // 查询用户是否已存在
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();
        userQueryWrapper.eq("username", user.getUsername())
                .or().eq("email", user.getEmail())
                .or().eq("phone", user.getPhone());
        boolean exists = userMapper.exists(userQueryWrapper);
        if (exists) {
            return Result.fail(MessageConstants.USER_EXISTS);
        }

        // 插入数据
        user.setState(1);
        userMapper.insert(user);
        stringRedisTemplate.delete(verifiedKey);
        //UserHolder.saveId(user);
        return Result.success();
    }

    @Override
    public Result login(UserLoginDTO userLoginDTO) {
        if (userLoginDTO == null) {
            return Result.fail(MessageConstants.ACCOUNT_FORMAT_ERROR);
        }
        String account = userLoginDTO.getAccount();
        String password = userLoginDTO.getPassword();
        QueryWrapper<User> userQueryWrapper = new QueryWrapper<>();

        // 校验密码格式
        if (RegexUtil.isPasswordInvalid(password)) {
            return Result.fail(MessageConstants.PASSWORD_FORMAT_ERROR);
        }

        // 判断account是手机号、邮箱还是用户名
        if (!RegexUtil.isPhoneInvalid(account)) {
            userQueryWrapper.eq("phone", account);
        } else if (!RegexUtil.isEmailInvalid(account)) {
            userQueryWrapper.eq("email", account);
        } else if (!RegexUtil.isUsernameInvalid(account)) {
            userQueryWrapper.eq("username", account);
        } else {
            return Result.fail(MessageConstants.ACCOUNT_FORMAT_ERROR);
        }

        // 查询用户是否存在
        List<User> userList = userMapper.selectList(userQueryWrapper);
        if (CollectionUtil.isEmpty(userList)) {
            return Result.fail(MessageConstants.USER_NOT_EXIST);
        }

        // 校验密码
        for (User user : userList) {

            //if (user.getPassword().equals(password)) {
            if (PasswordUtil.matches(user.getPassword(), password)) {
                Integer userId = user.getUserId();
                // 更改用户登录状态
                user.setState(1);
                userMapper.updateById(user);
                HashMap<String, Object> map = new HashMap<>();
                map.put("user_id", userId);
                map.put("token", jwtUtil.create(userId));
                return Result.success(map);
            }
        }

        // 密码错误
        return Result.fail(MessageConstants.PASSWORD_ERROR);
    }
}
