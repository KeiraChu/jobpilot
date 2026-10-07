package com.job.util;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Date;

@Component
public class JwtUtil {
    @Value("${security.jwt.secret}")
    private String secret;

    @Value("${security.jwt.expiration-seconds}")
    private long expirationSeconds;

    private SecretKey key() {
        return Keys.hmacShaKeyFor(secret.getBytes(StandardCharsets.UTF_8));
    }

    public String create(Integer userId) {
        Date now = new Date();
        return Jwts.builder().setSubject(String.valueOf(userId)).setIssuedAt(now)
                .setExpiration(new Date(now.getTime() + expirationSeconds * 1000))
                .signWith(key()).compact();
    }

    public Integer parseUserId(String token) {
        Claims claims = Jwts.parserBuilder().setSigningKey(key()).build()
                .parseClaimsJws(token).getBody();
        return Integer.valueOf(claims.getSubject());
    }
}
