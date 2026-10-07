package com.job.dto;

import lombok.Data;

import java.io.Serializable;

@Data
public class WorkExperienceDTO implements Serializable {
    private String company;
    private String position_kind;
    private String start_time;
    private String end_time;
    private String experience;
}
