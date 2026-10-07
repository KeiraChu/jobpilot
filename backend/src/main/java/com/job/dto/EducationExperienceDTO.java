package com.job.dto;

import lombok.Data;

import java.io.Serializable;

@Data
public class EducationExperienceDTO implements Serializable {
    private String school;
    private String degree;
    private String start_time;
    private String end_time;
    private String profession;
    private String experience;
}
