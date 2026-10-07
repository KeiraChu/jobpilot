package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
@TableName("resume_project_experience")
public class ProjectExperience implements Serializable {
    @TableId("user_id")
    private Integer userId;
    private String project;
    private String role;
    private Date startTime;
    private Date endTime;
    private String experience;
}
