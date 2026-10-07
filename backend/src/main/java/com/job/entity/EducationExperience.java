package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
@TableName("resume_education_experience")
public class EducationExperience implements Serializable {
    @TableId("user_id")
    private Integer userId;
    private String school;
    private String degree;
    private Date startTime;
    private Date endTime;
    private String profession;
    private String experience;
}
