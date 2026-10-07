package com.job.util;

import com.job.dto.EducationExperienceDTO;
import com.job.dto.ProjectExperienceDTO;
import com.job.dto.ResumeSubmitDTO;
import com.job.dto.WorkExperienceDTO;
import org.apache.poi.ss.usermodel.Row;
import org.apache.poi.ss.usermodel.Sheet;
import org.apache.poi.ss.usermodel.Workbook;
import org.apache.poi.xssf.usermodel.XSSFWorkbook;

import java.io.FileOutputStream;
import java.text.SimpleDateFormat;

public class ExcelUtil {
    public void generateExcel(ResumeSubmitDTO resumeSubmitDTO, String filePath) {
        try {
            // 创建工作簿
            Workbook workbook = new XSSFWorkbook();

            // 创建工作表
            Sheet sheet = workbook.createSheet("Resume");
            
            // 创建行和列
            for (int i = 0; i < 2; i++) {
                Row row = sheet.createRow(i);
                for (int j = 0; j < 26; j++) {
                    row.createCell(j);
                }
            }

            // 获取第一行
            Row row1 = sheet.getRow(0);
            // 获取第二行
            Row row2 = sheet.getRow(1);

            // 手动设置单元格的值
            row1.getCell(0).setCellValue("姓名");
            row2.getCell(0).setCellValue(resumeSubmitDTO.getUsername());

            row1.getCell(1).setCellValue("职位期望");
            row2.getCell(1).setCellValue(resumeSubmitDTO.getPosition_expect());

            row1.getCell(2).setCellValue("薪资要求");
            row2.getCell(2).setCellValue(resumeSubmitDTO.getSalary_expect());

            row1.getCell(3).setCellValue("性别");
            row2.getCell(3).setCellValue(resumeSubmitDTO.getSex());

            // 创建一个 SimpleDateFormat 对象，指定要输出的日期格式
            SimpleDateFormat dateFormat = new SimpleDateFormat("yyyyMMdd");

            row1.getCell(4).setCellValue("参加工作时间");
            // 使用 SimpleDateFormat 对象的 format 方法将 Date 对象格式化为字符串
            String startWorkTime = dateFormat.format(resumeSubmitDTO.getStart_work_time());
            row2.getCell(4).setCellValue(startWorkTime);

            row1.getCell(5).setCellValue("生日");
            String birthday = dateFormat.format(resumeSubmitDTO.getBirthday());
            row2.getCell(5).setCellValue(birthday);

            row1.getCell(6).setCellValue("邮箱");
            row2.getCell(6).setCellValue(resumeSubmitDTO.getEmail());

            row1.getCell(7).setCellValue("电话");
            row2.getCell(7).setCellValue(resumeSubmitDTO.getPhone());

            row1.getCell(8).setCellValue("微信号");
            row2.getCell(8).setCellValue(resumeSubmitDTO.getWx());

            row1.getCell(9).setCellValue("期望城市");
            row2.getCell(9).setCellValue(resumeSubmitDTO.getCity_expect());

            row1.getCell(10).setCellValue("籍贯");
            row2.getCell(10).setCellValue(resumeSubmitDTO.getFrom());

            row1.getCell(11).setCellValue("政治面貌");
            row2.getCell(11).setCellValue(resumeSubmitDTO.getPolitical_status());

            row1.getCell(12).setCellValue("专业技能");
            row2.getCell(12).setCellValue(resumeSubmitDTO.getSkill());

            EducationExperienceDTO education = resumeSubmitDTO.getEducation_experience();

            row1.getCell(13).setCellValue("学校名称");
            row2.getCell(13).setCellValue(education.getSchool());

            row1.getCell(14).setCellValue("学历");
            row2.getCell(14).setCellValue(education.getDegree());

            row1.getCell(15).setCellValue("在校时间段");
            String schoolPeriod = education.getStart_time() + "-" + education.getEnd_time();
            row2.getCell(15).setCellValue(schoolPeriod);

            row1.getCell(16).setCellValue("专业");
            row2.getCell(16).setCellValue(education.getProfession());

            row1.getCell(17).setCellValue("在校经历");
            row2.getCell(17).setCellValue(education.getExperience());

            WorkExperienceDTO work = resumeSubmitDTO.getWork_experience();

            row1.getCell(18).setCellValue("公司名称");
            row2.getCell(18).setCellValue(work.getCompany());

            row1.getCell(19).setCellValue("职位类型");
            row2.getCell(19).setCellValue(work.getPosition_kind());

            row1.getCell(20).setCellValue("在职时间");
            String workPeriod = work.getStart_time() + "-" + work.getEnd_time();
            row2.getCell(20).setCellValue(workPeriod);

            row1.getCell(21).setCellValue("工作经历");
            row2.getCell(21).setCellValue(work.getExperience());

            ProjectExperienceDTO project = resumeSubmitDTO.getProject_experience();

            row1.getCell(22).setCellValue("项目名称");
            row2.getCell(22).setCellValue(project.getProject());

            row1.getCell(23).setCellValue("项目角色");
            row2.getCell(23).setCellValue(project.getRole());

            row1.getCell(24).setCellValue("项目时间");
            String projectPeriod = project.getStart_time() + "-" + project.getEnd_time();
            row2.getCell(24).setCellValue(projectPeriod);

            row1.getCell(25).setCellValue("项目描述");
            row2.getCell(25).setCellValue(project.getExperience());

            // 保存工作簿到文件
            FileOutputStream fileOut = new FileOutputStream(filePath);
            workbook.write(fileOut);
            fileOut.close();

            // 提示信息
            System.out.println("Excel 文件已成功创建并保存到：" + filePath);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
