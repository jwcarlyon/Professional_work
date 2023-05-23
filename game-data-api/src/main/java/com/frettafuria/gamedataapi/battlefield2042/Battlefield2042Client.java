package com.frettafuria.gamedataapi.battlefield2042;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;

@Service

public class Battlefield2042Client {
    @Value("${game-data-api.battlefield-2042-api.key}")
    private String battlefield2042Key;

    @Autowired
    private RestTemplate battlefield2042Api;

    public Battlefield2042Client(RestTemplate battlefield2042Api) {
        this.battlefield2042Api = battlefield2042Api;
    }

    public String getPlayerByAccountId(Integer accountId, Battlefield2042PlatformType battlefield2042PlatformType) {
        HttpEntity<String> httpEntity = new HttpEntity<>(getBattlefield2042Headers());
        String battlefield2042Url = "https://api.gametools.network/openapi.json/bf2042";
        String queryParameters = String.format(
                "?raw=false&format_values=true&playerid=%d&platform=%s&skip_battlelog=false",
                accountId,
                battlefield2042PlatformType.toString().toLowerCase()
        );
        ResponseEntity<String> response = battlefield2042Api.exchange(
                String.format("%s/stats%s", battlefield2042Url, queryParameters),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        return response.getBody();
    }

    private HttpHeaders getBattlefield2042Headers() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", String.format("Bearer %s", battlefield2042Key));
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        return headers;
    }
}
