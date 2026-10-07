package com.job.client;

import com.job.config.AiServiceProperties;
import com.job.entity.Position;
import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.*;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;
import org.springframework.http.client.SimpleClientHttpRequestFactory;
import org.springframework.web.multipart.MultipartFile;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Component
public class AiServiceClient {
    private final AiServiceProperties properties;
    private final RestTemplate restTemplate;

    public AiServiceClient(AiServiceProperties properties) {
        this.properties = properties;
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        int timeoutMillis = Math.max(1, properties.getTimeoutSeconds()) * 1000;
        factory.setConnectTimeout(Math.min(timeoutMillis, 10000));
        factory.setReadTimeout(timeoutMillis);
        this.restTemplate = new RestTemplate(factory);
    }

    public Map<String, Object> parseText(String text, String targetRole) {
        Map<String, Object> body = new HashMap<>();
        body.put("text", text);
        body.put("target_role", targetRole == null ? "" : targetRole);
        return post("/v1/resumes/parse", body);
    }

    public Map<String, Object> parseFile(MultipartFile file, String targetRole) throws Exception {
        HttpHeaders headers = headers();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);
        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
        body.add("target_role", targetRole == null ? "" : targetRole);
        body.add("file", new ByteArrayResource(file.getBytes()) {
            @Override public String getFilename() { return file.getOriginalFilename(); }
        });
        ResponseEntity<Map> response = restTemplate.exchange(
                properties.getUrl() + "/v1/resumes/files", HttpMethod.POST,
                new HttpEntity<>(body, headers), Map.class);
        return response.getBody();
    }

    public Map<String, Object> recommend(Integer userId, Map<String, Object> profile, List<Position> positions) {
        Map<String, Object> body = new HashMap<>();
        body.put("user_id", String.valueOf(userId));
        body.put("profile", profile);
        body.put("top_k", 10);
        body.put("positions", positions.stream().map(position -> {
            Map<String, Object> value = new HashMap<>();
            value.put("position_id", position.getPositionId());
            value.put("company", position.getCompany());
            value.put("title", position.getTitle());
            value.put("salary", value(position.getSalary()));
            value.put("education", value(position.getEducation()));
            value.put("description", value(position.getDescription()));
            value.put("address", value(position.getAddress()));
            return value;
        }).collect(Collectors.toList()));
        return post("/v1/matches/recommend", body);
    }

    public Map<String, Object> careerPlan(Map<String, Object> profile, Map<String, Object> match) {
        Map<String, Object> body = new HashMap<>();
        body.put("profile", profile);
        body.put("match", match);
        body.put("horizon_days", 60);
        return post("/v1/workflows/career-plan", body);
    }

    private Map<String, Object> post(String path, Object body) {
        ResponseEntity<Map> response = restTemplate.exchange(properties.getUrl() + path, HttpMethod.POST,
                new HttpEntity<>(body, headers()), Map.class);
        return response.getBody();
    }

    private HttpHeaders headers() {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        headers.set("X-Internal-API-Key", properties.getInternalKey());
        return headers;
    }

    private String value(String value) {
        return value == null ? "" : value;
    }
}
