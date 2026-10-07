package com.job.config;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.job.util.JwtUtil;
import com.job.util.Result;
import com.job.util.UserHolder;
import org.springframework.http.HttpStatus;
import org.springframework.stereotype.Component;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.annotation.Resource;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@Component
public class AuthInterceptor implements HandlerInterceptor {
    @Resource
    private JwtUtil jwtUtil;
    @Resource
    private ObjectMapper objectMapper;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String authorization = request.getHeader("Authorization");
        if (authorization == null || !authorization.startsWith("Bearer ")) {
            unauthorized(response);
            return false;
        }
        try {
            UserHolder.saveId(jwtUtil.parseUserId(authorization.substring(7)));
            return true;
        } catch (Exception ignored) {
            unauthorized(response);
            return false;
        }
    }

    private void unauthorized(HttpServletResponse response) throws Exception {
        response.setStatus(HttpStatus.UNAUTHORIZED.value());
        response.setContentType("application/json;charset=UTF-8");
        response.getWriter().write(objectMapper.writeValueAsString(Result.fail(401, "登录状态无效或已过期")));
    }

    @Override
    public void afterCompletion(HttpServletRequest request, HttpServletResponse response, Object handler, Exception ex) {
        UserHolder.removeId();
    }
}
