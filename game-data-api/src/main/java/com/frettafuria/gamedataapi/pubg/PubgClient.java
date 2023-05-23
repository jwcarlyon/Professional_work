package com.frettafuria.gamedataapi.pubg;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;

@Service
public class PubgClient {
    @Value("${game-data-api.pubg-api.key}")
    private String pubgKey;
    @Autowired
    private RestTemplate pubgApi;

    public PubgClient(RestTemplate pubgApi) {
        this.pubgApi = pubgApi;
    }

    public String getPlayerByAccountId(String accountId, PubgPlatformType pubgPlatformType) {
        HttpEntity<String> httpEntity = new HttpEntity<>(getPubgHeaders());
        String pubgUrl = String.format("https://api.pubg.com/shards/%s", pubgPlatformType.toString().toLowerCase());
        ResponseEntity<String> response = pubgApi.exchange(
                String.format("%s/player/%s", pubgUrl, accountId),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        return response.getBody();
    }

    public String getMatchByMatchId(String matchId, PubgPlatformType pubgPlatformType) {
        HttpEntity<String> httpEntity = new HttpEntity<>(getPubgHeaders());
        String pubgUrl = String.format("https://api.pubg.com/shards/%s", pubgPlatformType.toString().toLowerCase());
        ResponseEntity<String> response = pubgApi.exchange(
                String.format("%s/matches/%s", pubgUrl, matchId),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        return response.getBody();
    }

    public String getTournamentByTournamentId(String tournamentId, PubgPlatformType pubgPlatformType) {
        HttpEntity<String> httpEntity = new HttpEntity<>(getPubgHeaders());
        String pubgUrl = String.format("https://api.pubg.com/shards/%s", pubgPlatformType.toString().toLowerCase());
        ResponseEntity<String> response = pubgApi.exchange(
                String.format("%s/tournaments/%s", pubgUrl, tournamentId),
                HttpMethod.GET,
                httpEntity,
                String.class
        );
        return response.getBody();
    }

    private HttpHeaders getPubgHeaders() {
        HttpHeaders headers = new HttpHeaders();
        headers.add("Authorization", String.format("Bearer %s", pubgKey));
        headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
        return headers;
    }
}
