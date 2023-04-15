package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.courses.GpLapTime;
import com.example.example_maven_springboot_fullstack.drivers.Driver;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.web.client.RestTemplate;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.when;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class ErgastClientTest {
    @Mock
    private RestTemplate mockErgastApi;
    @InjectMocks
    private ErgastClient ergastClient;
    @Nested
    class getAllDriversByYear {
        @Test
        @DisplayName(value = "When all drivers by year are requested, " +
                "then a request to ergastAPI is made and a list of drivers is deserialized and returned")
        void getsAllDriversByYear() throws Exception {
            String expectedResponse = "{\"MRData\":{\"xmlns\":\"http:\\/\\/ergast.com\\/mrd\\/1.5\",\"series\":\"f1\",\"url\":\"http://ergast.com/api/f1/2022/drivers.json\",\"limit\":\"30\",\"offset\":\"0\",\"total\":\"22\",\"DriverTable\":{\"season\":\"2022\",\"Drivers\":[{\"driverId\":\"albon\",\"permanentNumber\":\"23\",\"code\":\"ALB\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Alexander_Albon\",\"givenName\":\"Alexander\",\"familyName\":\"Albon\",\"dateOfBirth\":\"1996-03-23\",\"nationality\":\"Thai\"},{\"driverId\":\"alonso\",\"permanentNumber\":\"14\",\"code\":\"ALO\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Fernando_Alonso\",\"givenName\":\"Fernando\",\"familyName\":\"Alonso\",\"dateOfBirth\":\"1981-07-29\",\"nationality\":\"Spanish\"},{\"driverId\":\"bottas\",\"permanentNumber\":\"77\",\"code\":\"BOT\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Valtteri_Bottas\",\"givenName\":\"Valtteri\",\"familyName\":\"Bottas\",\"dateOfBirth\":\"1989-08-28\",\"nationality\":\"Finnish\"},{\"driverId\":\"de_vries\",\"permanentNumber\":\"45\",\"code\":\"DEV\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Nyck_de_Vries\",\"givenName\":\"Nyck\",\"familyName\":\"de Vries\",\"dateOfBirth\":\"1995-02-06\",\"nationality\":\"Dutch\"},{\"driverId\":\"gasly\",\"permanentNumber\":\"10\",\"code\":\"GAS\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Pierre_Gasly\",\"givenName\":\"Pierre\",\"familyName\":\"Gasly\",\"dateOfBirth\":\"1996-02-07\",\"nationality\":\"French\"},{\"driverId\":\"hamilton\",\"permanentNumber\":\"44\",\"code\":\"HAM\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Lewis_Hamilton\",\"givenName\":\"Lewis\",\"familyName\":\"Hamilton\",\"dateOfBirth\":\"1985-01-07\",\"nationality\":\"British\"},{\"driverId\":\"hulkenberg\",\"permanentNumber\":\"27\",\"code\":\"HUL\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Nico_H%C3%BClkenberg\",\"givenName\":\"Nico\",\"familyName\":\"Hülkenberg\",\"dateOfBirth\":\"1987-08-19\",\"nationality\":\"German\"},{\"driverId\":\"latifi\",\"permanentNumber\":\"6\",\"code\":\"LAT\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Nicholas_Latifi\",\"givenName\":\"Nicholas\",\"familyName\":\"Latifi\",\"dateOfBirth\":\"1995-06-29\",\"nationality\":\"Canadian\"},{\"driverId\":\"leclerc\",\"permanentNumber\":\"16\",\"code\":\"LEC\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Charles_Leclerc\",\"givenName\":\"Charles\",\"familyName\":\"Leclerc\",\"dateOfBirth\":\"1997-10-16\",\"nationality\":\"Monegasque\"},{\"driverId\":\"kevin_magnussen\",\"permanentNumber\":\"20\",\"code\":\"MAG\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Kevin_Magnussen\",\"givenName\":\"Kevin\",\"familyName\":\"Magnussen\",\"dateOfBirth\":\"1992-10-05\",\"nationality\":\"Danish\"},{\"driverId\":\"norris\",\"permanentNumber\":\"4\",\"code\":\"NOR\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Lando_Norris\",\"givenName\":\"Lando\",\"familyName\":\"Norris\",\"dateOfBirth\":\"1999-11-13\",\"nationality\":\"British\"},{\"driverId\":\"ocon\",\"permanentNumber\":\"31\",\"code\":\"OCO\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Esteban_Ocon\",\"givenName\":\"Esteban\",\"familyName\":\"Ocon\",\"dateOfBirth\":\"1996-09-17\",\"nationality\":\"French\"},{\"driverId\":\"perez\",\"permanentNumber\":\"11\",\"code\":\"PER\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Sergio_P%C3%A9rez\",\"givenName\":\"Sergio\",\"familyName\":\"Pérez\",\"dateOfBirth\":\"1990-01-26\",\"nationality\":\"Mexican\"},{\"driverId\":\"ricciardo\",\"permanentNumber\":\"3\",\"code\":\"RIC\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Daniel_Ricciardo\",\"givenName\":\"Daniel\",\"familyName\":\"Ricciardo\",\"dateOfBirth\":\"1989-07-01\",\"nationality\":\"Australian\"},{\"driverId\":\"russell\",\"permanentNumber\":\"63\",\"code\":\"RUS\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/George_Russell_%28racing_driver%29\",\"givenName\":\"George\",\"familyName\":\"Russell\",\"dateOfBirth\":\"1998-02-15\",\"nationality\":\"British\"},{\"driverId\":\"sainz\",\"permanentNumber\":\"55\",\"code\":\"SAI\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Carlos_Sainz_Jr.\",\"givenName\":\"Carlos\",\"familyName\":\"Sainz\",\"dateOfBirth\":\"1994-09-01\",\"nationality\":\"Spanish\"},{\"driverId\":\"mick_schumacher\",\"permanentNumber\":\"47\",\"code\":\"MSC\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Mick_Schumacher\",\"givenName\":\"Mick\",\"familyName\":\"Schumacher\",\"dateOfBirth\":\"1999-03-22\",\"nationality\":\"German\"},{\"driverId\":\"stroll\",\"permanentNumber\":\"18\",\"code\":\"STR\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Lance_Stroll\",\"givenName\":\"Lance\",\"familyName\":\"Stroll\",\"dateOfBirth\":\"1998-10-29\",\"nationality\":\"Canadian\"},{\"driverId\":\"tsunoda\",\"permanentNumber\":\"22\",\"code\":\"TSU\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Yuki_Tsunoda\",\"givenName\":\"Yuki\",\"familyName\":\"Tsunoda\",\"dateOfBirth\":\"2000-05-11\",\"nationality\":\"Japanese\"},{\"driverId\":\"max_verstappen\",\"permanentNumber\":\"33\",\"code\":\"VER\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Max_Verstappen\",\"givenName\":\"Max\",\"familyName\":\"Verstappen\",\"dateOfBirth\":\"1997-09-30\",\"nationality\":\"Dutch\"},{\"driverId\":\"vettel\",\"permanentNumber\":\"5\",\"code\":\"VET\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Sebastian_Vettel\",\"givenName\":\"Sebastian\",\"familyName\":\"Vettel\",\"dateOfBirth\":\"1987-07-03\",\"nationality\":\"German\"},{\"driverId\":\"zhou\",\"permanentNumber\":\"24\",\"code\":\"ZHO\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/Guanyu_Zhou\",\"givenName\":\"Guanyu\",\"familyName\":\"Zhou\",\"dateOfBirth\":\"1999-05-30\",\"nationality\":\"Chinese\"}]}}}\n";
            when(mockErgastApi.getForObject("http://ergast.com/api/f1/test/drivers.json", String.class)).thenReturn(expectedResponse);

            Driver[] result = ergastClient.getAllDriversByYear("test");

            assertEquals(result.length, 22);
        }
    }
    @Nested
    class getAllLapTimesFromGp {
        @Test
        @DisplayName(value = "When all lap times for a specific round, lap and year are requested, " +
                "then a request to ergastAPI is made and a list of courselaptimes is deserialized and returned")
        void getsAllLapTimesFromGp() {
            String expectedResponse = "{\"MRData\":{\"xmlns\":\"http:\\/\\/ergast.com\\/mrd\\/1.5\",\"series\":\"f1\",\"url\":\"http://ergast.com/api/f1/2022/1/laps/1.json\",\"limit\":\"30\",\"offset\":\"0\",\"total\":\"20\",\"RaceTable\":{\"season\":\"2022\",\"round\":\"1\",\"Races\":[{\"season\":\"2022\",\"round\":\"1\",\"url\":\"http:\\/\\/en.wikipedia.org\\/wiki\\/2022_Bahrain_Grand_Prix\",\"raceName\":\"Bahrain Grand Prix\",\"Circuit\":{\"circuitId\":\"bahrain\",\"url\":\"http://en.wikipedia.org/wiki/Bahrain_International_Circuit\",\"circuitName\":\"Bahrain International Circuit\",\"Location\":{\"lat\":\"26.0325\",\"long\":\"50.5106\",\"locality\":\"Sakhir\",\"country\":\"Bahrain\"}},\"date\":\"2022-03-20\",\"time\":\"15:00:00Z\",\"Laps\":[{\"number\":\"1\",\"Timings\":[{\"driverId\":\"leclerc\",\"position\":\"1\",\"time\":\"1:39.070\"},{\"driverId\":\"max_verstappen\",\"position\":\"2\",\"time\":\"1:40.236\"},{\"driverId\":\"sainz\",\"position\":\"3\",\"time\":\"1:41.006\"},{\"driverId\":\"hamilton\",\"position\":\"4\",\"time\":\"1:41.555\"},{\"driverId\":\"kevin_magnussen\",\"position\":\"5\",\"time\":\"1:42.333\"},{\"driverId\":\"perez\",\"position\":\"6\",\"time\":\"1:42.993\"},{\"driverId\":\"russell\",\"position\":\"7\",\"time\":\"1:43.445\"},{\"driverId\":\"gasly\",\"position\":\"8\",\"time\":\"1:44.270\"},{\"driverId\":\"alonso\",\"position\":\"9\",\"time\":\"1:45.174\"},{\"driverId\":\"ocon\",\"position\":\"10\",\"time\":\"1:46.170\"},{\"driverId\":\"albon\",\"position\":\"11\",\"time\":\"1:47.636\"},{\"driverId\":\"tsunoda\",\"position\":\"12\",\"time\":\"1:48.128\"},{\"driverId\":\"mick_schumacher\",\"position\":\"13\",\"time\":\"1:48.826\"},{\"driverId\":\"bottas\",\"position\":\"14\",\"time\":\"1:49.195\"},{\"driverId\":\"hulkenberg\",\"position\":\"15\",\"time\":\"1:49.698\"},{\"driverId\":\"norris\",\"position\":\"16\",\"time\":\"1:50.088\"},{\"driverId\":\"stroll\",\"position\":\"17\",\"time\":\"1:50.439\"},{\"driverId\":\"latifi\",\"position\":\"18\",\"time\":\"1:51.134\"},{\"driverId\":\"zhou\",\"position\":\"19\",\"time\":\"1:51.374\"},{\"driverId\":\"ricciardo\",\"position\":\"20\",\"time\":\"1:51.601\"}]}]}]}}}";
            when(mockErgastApi.getForObject("http://ergast.com/api/f1/testSeason/testRound/laps/1.json", String.class)).thenReturn(expectedResponse);

            ArrayList<GpLapTime[]> result = ergastClient.getAllLapTimesFromGp("testSeason", "testRound");

            assertEquals(result.size(), 0);//TODO: fix this test
        }
    }
}