package com.job.constant;

public class RedisConstants {
    public static final String REGISTER_CODE_KEY = "jobpilot:register:code:";
    public static final String REGISTER_VERIFIED_KEY = "jobpilot:register:verified:";
    public static final String REGISTER_RATE_KEY = "jobpilot:register:rate:";
    public static final Long REGISTER_CODE_TTL = 5L;
    public static final Long REGISTER_VERIFIED_TTL = 10L;

    public static final String STATISTIC_KEY = "jobpilot:statistic";
    public static final String STATISTIC_AVAILABLE_POSITION = "available_position";
    public static final String STATISTIC_COMPANY_AMOUNT = "company_amount";
}
