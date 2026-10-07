package com.job.config;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.stereotype.Component;

@Data
@Component
@ConfigurationProperties(prefix = "ai.service")
public class AiServiceProperties {
    private String url;
    private String internalKey;
    private int timeoutSeconds = 60;
}
