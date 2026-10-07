package com.job.controller;

import com.job.service.CommonService;
import com.job.util.Result;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Param;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.util.Map;

/**
 * 通用接口
 */
@RestController
@Slf4j
public class CommonController {
    @Resource
    private CommonService commonService;

    @GetMapping("/get_statistic")
    public Result getStatistic() {
        Map<String, Integer> statistic = commonService.getStatistic();
        return Result.success(statistic);
    }
}
