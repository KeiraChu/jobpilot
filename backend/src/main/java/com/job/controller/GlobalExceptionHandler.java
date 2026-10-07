package com.job.controller;

import com.job.util.Result;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@Slf4j
@RestControllerAdvice
public class GlobalExceptionHandler {
    @ExceptionHandler(MethodArgumentNotValidException.class)
    public Result validation(MethodArgumentNotValidException exception) {
        return Result.fail(HttpStatus.BAD_REQUEST.value(), "请求参数不合法");
    }

    @ExceptionHandler(Exception.class)
    public Result unexpected(Exception exception) {
        log.error("未处理异常", exception);
        return Result.fail(HttpStatus.INTERNAL_SERVER_ERROR.value(), "服务暂时不可用");
    }
}
