package com.job;

import com.job.dto.ResumeSubmitDTO;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.lang.reflect.Field;

@SpringBootTest
public class ReflectTest {
    //@Test
    void testReflect() {
        ResumeSubmitDTO resumeSubmitDTO = new ResumeSubmitDTO();

        // 使用反射获取ResumeSubmitDTO的所有属性并打印它们的值
        Class<?> clazz = resumeSubmitDTO.getClass();
        Field[] fields = clazz.getDeclaredFields();
        for (Field field : fields) {
            field.setAccessible(true); // 设置属性可访问
            try {
                Object value = field.get(resumeSubmitDTO); // 获取属性值
                System.out.println(field.getName() + ": " + value);
            } catch (IllegalAccessException e) {
                e.printStackTrace();
            }
        }
    }
}
