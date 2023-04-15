package com.example.example_maven_springboot_fullstack.rapid;

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
class RapidClientTest {
    @Mock
    private RestTemplate mockRapidApi;
    @InjectMocks
    private RapidClient rapidClient;
    @BeforeAll
    void setup() {
        ReflectionTestUtils.setField(rapidClient, "rapidApiKey", "testKey");
    }
    @Nested
    class getDriverByName {
        @Test
        @DisplayName(value = "When drivers by name are requested, " +
                "then a request to rapidAPI is made and a list of drivers is deserialized and returned")
        void getDriverByName() {
            String expectedResponse = "{\"get\":\"drivers\",\"parameters\":{\"search\":\"russel\"},\"errors\":[],\"results\":1,\"response\":[{\"id\":51,\"name\":\"George Russell\",\"abbr\":\"RUS\",\"image\":\"https:\\/\\/media-3.api-sports.io\\/formula-1\\/drivers\\/51.png\",\"nationality\":\"British\",\"country\":{\"name\":\"United Kingdom\",\"code\":\"GB\"},\"birthdate\":\"1998-02-15\",\"birthplace\":\"King's Lynn, England\",\"number\":63,\"grands_prix_entered\":85,\"world_championships\":0,\"podiums\":9,\"highest_race_finish\":{\"position\":1,\"number\":1},\"highest_grid_position\":1,\"career_points\":\"312\",\"teams\":[{\"season\":2023,\"team\":{\"id\":5,\"name\":\"Mercedes-AMG Petronas\",\"logo\":\"https:\\/\\/media-2.api-sports.io\\/formula-1\\/teams\\/5.png\"}},{\"season\":2022,\"team\":{\"id\":5,\"name\":\"Mercedes-AMG Petronas\",\"logo\":\"https:\\/\\/media-2.api-sports.io\\/formula-1\\/teams\\/5.png\"}},{\"season\":2021,\"team\":{\"id\":12,\"name\":\"Williams F1 Team\",\"logo\":\"https:\\/\\/media-3.api-sports.io\\/formula-1\\/teams\\/12.png\"}},{\"season\":2020,\"team\":{\"id\":12,\"name\":\"Williams F1 Team\",\"logo\":\"https:\\/\\/media-3.api-sports.io\\/formula-1\\/teams\\/12.png\"}},{\"season\":2019,\"team\":{\"id\":12,\"name\":\"Williams F1 Team\",\"logo\":\"https:\\/\\/media-3.api-sports.io\\/formula-1\\/teams\\/12.png\"}}]}]}";
            HttpHeaders headers = new HttpHeaders();
            headers.setAccept(Collections.singletonList(MediaType.APPLICATION_JSON));
            headers.add("X-RapidAPI-Key", "testKey");
            headers.add("X-RapidAPI-Host", "api-formula-1.p.rapidapi.com");
            HttpEntity<String> httpEntity = new HttpEntity<>(headers);
            when(mockRapidApi.exchange(
                    "https://api-formula-1.p.rapidapi.com/drivers?search=test",
                    HttpMethod.GET,
                    httpEntity,
                    String.class
            )).thenReturn(ResponseEntity.ok(expectedResponse));

            String response = rapidClient.getDriverByName("test");

            assertEquals(expectedResponse, response);
        }
    }
}