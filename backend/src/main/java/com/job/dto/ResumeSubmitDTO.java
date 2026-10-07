package com.job.dto;

import lombok.Data;

import java.io.Serializable;
import java.util.Date;

@Data
public class ResumeSubmitDTO implements Serializable {
    private Integer userId;
    private String username;
    private String email;
    private String phone;
    private String wx;
    private String salary_expect;
    private String position_expect;
    private String sex;
    private Date start_work_time;
    private Date birthday;
    private String city_expect;
    private String from;
    private String political_status;

    private String skill;

    private EducationExperienceDTO education_experience;
    private WorkExperienceDTO work_experience;
    private ProjectExperienceDTO project_experience;
}
