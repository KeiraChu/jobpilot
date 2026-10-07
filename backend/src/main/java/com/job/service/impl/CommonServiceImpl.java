package com.job.service.impl;

import cn.hutool.core.util.StrUtil;
import com.job.constant.RedisConstants;
import com.job.mapper.CommonMapper;
import com.job.service.CommonService;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.stereotype.Service;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.Map;

@Service
public class CommonServiceImpl implements CommonService {
    @Resource
    private CommonMapper commonMapper;

    @Resource
    private StringRedisTemplate stringRedisTemplate;

    @Override
    public Map<String, Integer> getStatistic() {
        Map<String, Integer> map = new HashMap<>();
        String key = RedisConstants.STATISTIC_KEY;
        String hashKey1 = RedisConstants.STATISTIC_AVAILABLE_POSITION;
        String hashKey2 = RedisConstants.STATISTIC_COMPANY_AMOUNT;

        Object availablePosition = stringRedisTemplate.opsForHash().get(key, hashKey1);
        Object companyAmount = stringRedisTemplate.opsForHash().get(key, hashKey2);

        if (availablePosition == null) {
            availablePosition = commonMapper.getAvailablePosition().toString();
            stringRedisTemplate.opsForHash().put(key, hashKey1, availablePosition);
        }

        if (companyAmount == null) {
            companyAmount = commonMapper.getCompanyAmount().toString();
            stringRedisTemplate.opsForHash().put(key, hashKey2, companyAmount);
        }

        map.put(hashKey1, Integer.parseInt(availablePosition.toString()));
        map.put(hashKey2, Integer.parseInt(companyAmount.toString()));
        return map;
    }
}
