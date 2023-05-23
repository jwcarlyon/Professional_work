package com.frettafuria.gamedataapi.battlefield2042;

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

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class Battlefield2042ClientTest {

    @Mock
    private RestTemplate mockBattlefield2042Api;
    @InjectMocks
    private Battlefield2042Client battlefield2042Client;

    @BeforeAll
    void setup() {
        ReflectionTestUtils.setField(battlefield2042Client, "battlefield2042Key", "testKey");
    }

    @Nested
    class getPlayerByAccountId {
        @Test
        @DisplayName("When a player is requested by player-id with a platformType, " +
                "Then the player's raw json response is returned.")
        void returnsMatchResponse() {
            String expectedResponse = "testPlayerStatsResponse";
            HttpHeaders headers = new HttpHeaders();
            headers.add("Authorization", "Bearer testKey");
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            HttpEntity<String> httpEntity = new HttpEntity<>(headers);
            when(mockBattlefield2042Api.exchange(
                    "https://api.gametools.network/openapi.json/bf2042/stats?raw=false&format_values=true&playerid=1234567&platform=ps4&skip_battlelog=false",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = battlefield2042Client.getPlayerByAccountId(1234567, Battlefield2042PlatformType.PS4);

            assertEquals(expectedResponse, response);
        }
    }
}