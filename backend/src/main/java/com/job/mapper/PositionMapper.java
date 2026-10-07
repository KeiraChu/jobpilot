package com.job.mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.job.entity.Position;
import org.apache.ibatis.annotations.Mapper;

import java.util.List;

@Mapper
public interface PositionMapper extends BaseMapper<Position> {
    List<Position> queryPositionByCompanyWithTitle(List<String> list);
}
