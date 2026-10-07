package com.job;

import com.job.util.PasswordUtil;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

class PasswordUtilTest {
    @Test
    void bcryptUsesSaltAndVerifiesRawPassword() {
        String first = PasswordUtil.encode("Valid123?");
        String second = PasswordUtil.encode("Valid123?");

        assertNotEquals(first, second);
        assertTrue(PasswordUtil.matches(first, "Valid123?"));
        assertFalse(PasswordUtil.matches(first, "Wrong123?"));
    }
}
