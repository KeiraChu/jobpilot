package com.job.controller;

import com.job.entity.Position;
import com.job.entity.RecommendationFeedback;
import com.job.mapper.PositionMapper;
import com.job.mapper.RecommendationFeedbackMapper;
import com.job.util.Result;
import com.job.util.UserHolder;
import org.springframework.web.bind.annotation.*;

import javax.annotation.Resource;
import java.time.LocalDateTime;
import java.util.Map;

@RestController
@RequestMapping("/positions")
public class PositionController {
    @Resource
    private PositionMapper positionMapper;
    @Resource
    private RecommendationFeedbackMapper feedbackMapper;

    @GetMapping
    public Result list() {
        return Result.success(positionMapper.selectList(null));
    }

    @PostMapping
    public Result publish(@RequestBody Position position) {
        if (position == null || isBlank(position.getCompany()) || isBlank(position.getTitle()) || isBlank(position.getDescription())) {
            return Result.fail("公司、职位名称和职位描述不能为空");
        }
        position.setPositionId(null);
        positionMapper.insert(position);
        return Result.success(position);
    }

    @PostMapping("/{positionId}/feedback")
    public Result feedback(@PathVariable Integer positionId, @RequestBody Map<String, String> body) {
        if (positionMapper.selectById(positionId) == null) {
            return Result.fail(404, "职位不存在");
        }
        if (body == null) {
            return Result.fail("反馈内容不能为空");
        }
        String action = body.get("action");
        if (action == null || !(action.equals("LIKE") || action.equals("DISLIKE") || action.equals("APPLIED"))) {
            return Result.fail("action 必须是 LIKE、DISLIKE 或 APPLIED");
        }
        RecommendationFeedback feedback = new RecommendationFeedback();
        feedback.setUserId(UserHolder.getId());
        feedback.setPositionId(positionId);
        feedback.setAction(action);
        feedback.setReason(body.get("reason"));
        feedback.setCreatedAt(LocalDateTime.now());
        feedbackMapper.insert(feedback);
        return Result.success();
    }

    private boolean isBlank(String value) {
        return value == null || value.trim().isEmpty();
    }
}
