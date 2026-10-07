package com.job.controller;

import com.job.client.AiServiceClient;
import com.job.entity.Position;
import com.job.mapper.PositionMapper;
import com.job.util.Result;
import com.job.util.UserHolder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.annotation.Resource;
import java.util.Map;
import java.util.List;

@RestController
@RequestMapping("/ai")
public class AiCareerController {
    @Resource
    private AiServiceClient client;
    @Resource
    private PositionMapper positionMapper;

    @PostMapping("/recommend")
    @SuppressWarnings("unchecked")
    public Result recommend(@RequestBody Map<String, Object> request) {
        Object profile = request == null ? null : request.get("profile");
        if (!(profile instanceof Map)) {
            return Result.fail("请先确认简历能力画像");
        }
        Integer userId = UserHolder.getId();
        if (userId == null) {
            return Result.fail(401, "请先登录");
        }
        try {
            List<Position> positions = positionMapper.selectList(null);
            Map<String, Object> response = client.recommend(userId, (Map<String, Object>) profile, positions);
            response.put("profile", profile);
            return Result.success(response);
        } catch (Exception e) {
            return Result.fail(503, "职位推荐失败，请稍后重试");
        }
    }

    @PostMapping("/career-plan")
    @SuppressWarnings("unchecked")
    public Result careerPlan(@RequestBody Map<String, Object> request) {
        Object profile = request.get("profile");
        Object match = request.get("match");
        if (!(profile instanceof Map) || !(match instanceof Map)) {
            return Result.fail("profile 和 match 不能为空");
        }
        try {
            return Result.success(client.careerPlan((Map<String, Object>) profile, (Map<String, Object>) match));
        } catch (Exception e) {
            return Result.fail(503, "求职计划生成失败，请稍后重试");
        }
    }
}
