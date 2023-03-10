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

import static org.junit.jupiter.api.Assertions.assertEquals;
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
        void getCourseList() {
            when(mockErgastClient.getAllCoursesBySeason("2022")).thenReturn("courses list for 2022");

            String result = coursesService.getCourseList("2022");

            assertEquals(result, "courses list for 2022");
        }
    }
}