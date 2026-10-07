package com.job.mapper;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface CommonMapper {
    @Select("select count(position_id) as available_position from positions;")
    Integer getAvailablePosition();

    @Select("select count(DISTINCT company) as unique_companies_count from positions;")
    Integer getCompanyAmount();
}
