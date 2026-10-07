package com.job;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.data.redis.core.StringRedisTemplate;

import javax.annotation.Resource;

@SpringBootTest
public class RedisTest {
    @Resource
    private StringRedisTemplate stringRedisTemplate;

    //@Test
    void testHash() {
        String key = "test";
        String hashKey1 = "positions";
        String hashKey2 = "companys";
        stringRedisTemplate.opsForHash().put(key, hashKey1, "2872");
        stringRedisTemplate.opsForHash().put(key, hashKey2, "650");

        //Integer positions = Integer.parseInt(stringRedisTemplate.opsForHash().get(key, hashKey1).toString());
        String positions = stringRedisTemplate.opsForHash().get(key, hashKey1).toString();
        System.out.println("positions = " + positions);


        //Integer companys = stringRedisTemplate.opsForHash().get(key, hashKey2);
        String companys = stringRedisTemplate.opsForHash().get(key, hashKey2).toString();
        System.out.println("companys = " + companys);
    }
}
