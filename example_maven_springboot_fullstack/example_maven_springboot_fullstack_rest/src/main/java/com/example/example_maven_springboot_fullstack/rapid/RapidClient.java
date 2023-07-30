package com.example.example_maven_springboot_fullstack.rapid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;

@Service
public class RapidClient {
    @Value("${example-maven-springboot-fullstack.rapid-api.key}")
    private String rapidApiKey;
    @Autowired
    private RestTemplate rapidAPI;

    public RapidClient(RestTemplate rapidAPI) {
        this.rapidAPI = rapidAPI;
    }

    public String getDriverByName(String name) {
        HttpHeaders headers = new HttpHeaders();
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        headers.add("X-RapidAPI-Key", rapidApiKey);
        headers.add("X-RapidAPI-Host", "api-formula-1.p.rapidapi.com");
        HttpEntity<String> httpEntity = new HttpEntity<>(headers);
        ResponseEntity<String> response = rapidAPI.exchange(
                String.format("https://api-formula-1.p.rapidapi.com/drivers?search=%s", name),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        System.out.println("Converting Rapid response : " + response);
        return response.getBody();
    }
}
