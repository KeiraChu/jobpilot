package com.job.entity;

import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.io.Serializable;

@Data
@TableName("positions")
public class Position implements Serializable {
    @TableId("position_id")
    private Integer positionId;

    private String company;

    private String title;

    private String salary;

    private String education;

    private String description;

    private String hiringManager;

    private String lastActive;

    private String address;
}
