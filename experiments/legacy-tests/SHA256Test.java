package com.job;

import cn.hutool.crypto.digest.DigestUtil;
import org.junit.jupiter.api.Test;

public class SHA256Test {
    //@Test
    void testSHA256() {
        String password1 = "QZH123456@";
        String sha256Hex1 = DigestUtil.sha256Hex(password1);
        System.out.println("sha256Hex1 = " + sha256Hex1);

        String password2 = "QZH654321@";
        String sha256Hex2 = DigestUtil.sha256Hex(password2);
        System.out.println("sha256Hex2 = " + sha256Hex2);

        if (sha256Hex1.equals(sha256Hex2)) {
            System.out.println("password1 == password2");
        } else {
            System.out.println("password1 != password2");
        }
    }
}
