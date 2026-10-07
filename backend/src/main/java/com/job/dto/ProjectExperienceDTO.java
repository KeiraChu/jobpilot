package com.job.dto;

import lombok.Data;

import java.io.Serializable;

@Data
public class ProjectExperienceDTO implements Serializable {
    private String project;
    private String role;
    private String start_time;
    private String end_time;
    private String experience;
}
