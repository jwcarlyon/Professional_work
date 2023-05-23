package com.frettafuria.gamedataapi.haloinfinite;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;

@Service
public class HaloInfiniteClient {
    @Value("${game-data-api.halo-infintie-api.key}")
    private String haloInfiniteKey;

    @Autowired
    private RestTemplate haloInfiniteApi;
    public HaloInfiniteClient(RestTemplate haloInfiniteApi) { this.haloInfiniteApi = haloInfiniteApi; }

    public String getMatchByMatchId(String matchId) {
        HttpEntity<String> httpEntity = new HttpEntity<>(getHaloInfiniteHeaders());
        String haloInfiniteUrl = "https://halo.api.stdlib.com/infinite@1.7.3/stats";
        ResponseEntity<String> response = haloInfiniteApi.exchange(
                String.format("%s/matches/%s", haloInfiniteUrl, matchId),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        return response.getBody();
    }

    private HttpHeaders getHaloInfiniteHeaders() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", String.format("Bearer %s", haloInfiniteKey));
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        return headers;
    }

}
