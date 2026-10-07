package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Builder;
import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
@Builder
@TableName("resume_personal_message")
public class PersonalMessage implements Serializable {
    @TableId("user_id")
    private Integer userId;
    private String username;
    private String positionExpect;
    private String salaryExpect;
    private String sex;
    private Date startWorkTime;
    private Date birthday;
    private String email;
    private String phone;
    private String wx;
    private String cityExpect;
    @TableField("hometown")
    private String from;
    private String politicalStatus;
}
