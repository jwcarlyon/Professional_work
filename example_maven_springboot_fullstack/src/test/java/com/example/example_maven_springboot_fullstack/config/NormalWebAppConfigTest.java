package com.example.example_maven_springboot_fullstack.config;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.web.client.RestTemplate;

import static org.junit.jupiter.api.Assertions.assertEquals;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class NormalWebAppConfigTest
{
    private NormalWebAppConfig normalWebAppConfig;

    @BeforeEach
    void setUp() { normalWebAppConfig = new NormalWebAppConfig(); }
    @Nested
    class restTemplate {
        @Test
        @DisplayName(value = "When a restTemplate is requested, then the RestTemplate type is returned")
        void returnsRestTemplate() {
            RestTemplate result = normalWebAppConfig.restTemplate(new RestTemplateBuilder());

            assertEquals(RestTemplate.class, result.getClass());
        }
    }
}
