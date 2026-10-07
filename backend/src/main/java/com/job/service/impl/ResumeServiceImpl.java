package com.job.service.impl;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.job.client.AiServiceClient;
import com.job.dto.ResumeSubmitDTO;
import com.job.entity.Position;
import com.job.mapper.PositionMapper;
import com.job.service.ResumeService;
import com.job.util.Result;
import com.job.util.UserHolder;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import javax.annotation.Resource;
import java.util.List;
import java.util.Map;
import java.util.Locale;
import java.util.Arrays;

@Service
@Slf4j
public class ResumeServiceImpl implements ResumeService {
    @Resource
    private PositionMapper positionMapper;
    @Resource
    private AiServiceClient aiServiceClient;
    @Resource
    private ObjectMapper objectMapper;

    @Override
    public Result saveResume(ResumeSubmitDTO resume) {
        Integer userId = UserHolder.getId();
        if (userId == null) {
            return Result.fail(401, "请先登录");
        }
        resume.setUserId(userId);
        try {
            String text = objectMapper.writeValueAsString(resume);
            Map<String, Object> profile = aiServiceClient.parseText(text, resume.getPosition_expect());
            return Result.success(buildResponse(profile));
        } catch (Exception e) {
            log.error("AI 推荐失败，userId={}", userId, e);
            return Result.fail(503, "推荐服务暂时不可用，请稍后重试");
        }
    }

    @Override
    public Result upload(MultipartFile file, String targetRole) {
        Integer userId = UserHolder.getId();
        if (userId == null) {
            return Result.fail(401, "请先登录");
        }
        if (file == null || file.isEmpty()) {
            return Result.fail("请选择简历文件");
        }
        if (file.getSize() > 20L * 1024 * 1024) {
            return Result.fail(413, "文件不能超过20MB");
        }
        String filename = file.getOriginalFilename() == null ? "" : file.getOriginalFilename().toLowerCase(Locale.ROOT);
        if (Arrays.stream(new String[]{".pdf", ".docx", ".txt", ".md"}).noneMatch(filename::endsWith)) {
            return Result.fail(415, "仅支持 PDF、DOCX、TXT、Markdown 简历");
        }
        try {
            Map<String, Object> profile = aiServiceClient.parseFile(file, targetRole);
            return Result.success(buildResponse(profile));
        } catch (Exception e) {
            log.error("简历解析或推荐失败，userId={}", userId, e);
            return Result.fail(503, "简历解析或推荐失败，请检查文件格式后重试");
        }
    }

    private Map<String, Object> buildResponse(Map<String, Object> profile) {
        List<Position> positions = positionMapper.selectList(null);
        Map<String, Object> response = aiServiceClient.recommend(UserHolder.getId(), profile, positions);
        response.put("profile", profile);
        return response;
    }
}
