package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
@TableName("resume_work_experience")
public class WorkExperience implements Serializable {
    @TableId("user_id")
    private Integer userId;
    private String company;
    @TableField("position")
    private String positionKind;
    private Date startTime;
    private Date endTime;
    private String experience;
}
