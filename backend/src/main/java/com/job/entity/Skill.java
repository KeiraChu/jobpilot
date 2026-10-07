package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Builder;
import lombok.Data;

import java.io.Serializable;

@Data
@Builder
@TableName("resume_skill")
public class Skill implements Serializable {
    @TableId("user_id")
    private Integer userId;
    private String skill;
}
