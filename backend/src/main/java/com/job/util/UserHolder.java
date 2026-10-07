package com.job.util;

import com.job.entity.User;

public class UserHolder {
    private static final ThreadLocal<Integer> tl = new ThreadLocal<>();

    public static void saveId(Integer userId) {
        tl.set(userId);
    }

    public static Integer getId() {
        return tl.get();
    }

    public static void removeId() {
        tl.remove();
    }
}
