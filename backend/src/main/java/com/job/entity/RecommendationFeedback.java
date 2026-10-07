package com.job.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@TableName("recommendation_feedback")
public class RecommendationFeedback {
    @TableId(type = IdType.AUTO)
    private Long id;
    private Integer userId;
    private Integer positionId;
    private String action;
    private String reason;
    private LocalDateTime createdAt;
}
