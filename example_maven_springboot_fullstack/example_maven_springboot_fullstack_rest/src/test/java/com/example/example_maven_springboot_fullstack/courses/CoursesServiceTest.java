package com.example.example_maven_springboot_fullstack.courses;

import com.example.example_maven_springboot_fullstack.ergast.ErgastClient;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.test.context.junit.jupiter.SpringExtension;

import java.util.ArrayList;
import java.util.Collections;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.when;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class CoursesServiceTest {
    @Mock
    private ErgastClient mockErgastClient;
    @InjectMocks
    private CoursesService coursesService;

    @Nested
    class getCourseList {
        @Test
        @DisplayName("When course list is requested by season, then that season's course list is returned")
        void returnsCourseList() {
            GpLapTime expectedGpLapTime = new GpLapTime();
            expectedGpLapTime.setDriverId("testId");
            expectedGpLapTime.setTime("testTime");
            expectedGpLapTime.setMysql_id(0);
            expectedGpLapTime.setPosition("testPosition");
            GpLapTime[] expectedGpLapTimeArray = { expectedGpLapTime };
            ArrayList<GpLapTime[]> expectedLapTimes = new ArrayList<>(Collections.singleton(expectedGpLapTimeArray));
            when(mockErgastClient.getAllLapTimesFromGp("2022", "1")).thenReturn(expectedLapTimes);

            String result = coursesService.getGpLapTimes("2022", "1");

            assertTrue(expectedLapTimes.toString().equals(result));
        }
    }
}