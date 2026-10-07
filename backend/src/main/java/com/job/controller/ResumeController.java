package com.job.controller;

import com.job.dto.ResumeSubmitDTO;
import com.job.service.ResumeService;
import com.job.util.Result;
import lombok.extern.slf4j.Slf4j;
import org.apache.ibatis.annotations.Param;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;

@RestController
@Slf4j
public class ResumeController {
    @Resource
    private ResumeService resumeService;

    @PostMapping("/resume/submit")
    public Result submit(@RequestBody ResumeSubmitDTO resumeSubmitDTO) {
//        Integer userId = UserHolder.getId();
//        System.out.println("userId = " + userId);

        return resumeService.saveResume(resumeSubmitDTO);
    }

    @PostMapping("/upload")
    public Result upload(@Param("file") MultipartFile file,
                         @Param("targetRole") String targetRole) {
        log.info("收到简历文件，name={}, size={}", file.getOriginalFilename(), file.getSize());
        return resumeService.upload(file, targetRole);
    }
}
