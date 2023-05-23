package com.frettafuria.gamedataapi.pubg;

import org.junit.jupiter.api.*;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.*;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.util.ReflectionTestUtils;
import org.springframework.web.client.RestTemplate;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.when;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class PubgClientTest {
    @Mock
    private RestTemplate mockPubgApi;
    @InjectMocks
    private PubgClient pubgClient;

    @BeforeAll
    void setup() {
        ReflectionTestUtils.setField(pubgClient, "pubgKey", "testKey");
    }

    @Nested
    class getMatchByMatchId {
        @Test
        @DisplayName("When a match is requested by match-id with a platformType, " +
                "Then the match's raw json response is returned.")
        void returnsMatchResponse() {
            String expectedResponse = "testMatchResponse";
            HttpHeaders headers = new HttpHeaders();
            headers.add("Authorization", "Bearer testKey");
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            HttpEntity<String> httpEntity = new HttpEntity<>(headers);
            when(mockPubgApi.exchange(
                    "https://api.pubg.com/shards/kakao/matches/match-id",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = pubgClient.getMatchByMatchId("match-id", PubgPlatformType.KAKAO);

            assertEquals(expectedResponse, response);
        }
    }
    @Nested
    class getPlayerByAccountId {
        @Test
        @DisplayName("When a player is requested by accountId with a platformType, " +
                "Then the player's raw json response is returned.")
        void returnsPlayerResponse() {
            String expectedResponse = "testPlayerResponse";
            HttpHeaders headers = new HttpHeaders();
            headers.add("Authorization", "Bearer testKey");
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            HttpEntity<String> httpEntity = new HttpEntity<>(headers);
            when(mockPubgApi.exchange(
                    "https://api.pubg.com/shards/kakao/player/player-id",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = pubgClient.getPlayerByAccountId("player-id", PubgPlatformType.KAKAO);

            assertEquals(expectedResponse, response);
        }
    }
    @Nested
    class getTournamentByTournamentId {
        @Test
        @DisplayName("When a tournament is requested by accountId with a platformType, " +
                "Then the tournament raw json response is returned.")
        void returnsTournamentResponse() {
            String expectedResponse = "testPlayerResponse";
            HttpHeaders headers = new HttpHeaders();
            headers.add("Authorization", "Bearer testKey");
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            HttpEntity<String> httpEntity = new HttpEntity<>(headers);
            when(mockPubgApi.exchange(
                    "https://api.pubg.com/shards/kakao/tournaments/tournament-id",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = pubgClient.getTournamentByTournamentId("tournament-id", PubgPlatformType.KAKAO);

            assertEquals(expectedResponse, response);
        }
    }
}