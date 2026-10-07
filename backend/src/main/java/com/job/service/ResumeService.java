package com.job.service;

import com.job.dto.ResumeSubmitDTO;
import com.job.util.Result;
import org.springframework.web.multipart.MultipartFile;

public interface ResumeService {
    Result saveResume(ResumeSubmitDTO resumeSubmitDTO);

    Result upload(MultipartFile file, String targetRole);
}
