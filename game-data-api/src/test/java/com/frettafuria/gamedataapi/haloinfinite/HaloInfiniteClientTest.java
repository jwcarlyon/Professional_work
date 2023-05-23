package com.frettafuria.gamedataapi.haloinfinite;

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
class HaloInfiniteClientTest {
    @Mock
    private RestTemplate mockHaloInfiniteApi;
    @InjectMocks
    private HaloInfiniteClient haloInfiniteClient;

    @BeforeAll
    void setup() {
        ReflectionTestUtils.setField(haloInfiniteClient, "haloInfiniteKey", "testKey");
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
            when(mockHaloInfiniteApi.exchange(
                    "https://halo.api.stdlib.com/infinite@1.7.3/stats/matches/match-id",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = haloInfiniteClient.getMatchByMatchId("match-id");

            assertEquals(expectedResponse, response);
        }
    }
}