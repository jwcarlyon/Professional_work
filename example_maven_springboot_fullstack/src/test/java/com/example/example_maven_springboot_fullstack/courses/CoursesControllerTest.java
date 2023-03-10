package com.example.example_maven_springboot_fullstack.courses;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit.jupiter.SpringExtension;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.result.MockMvcResultMatchers;
import org.springframework.test.web.servlet.setup.MockMvcBuilders;

import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class CoursesControllerTest {
    private MockMvc mockMvc;
    @Mock
    private CoursesService mockCoursesService;
    @InjectMocks
    private CoursesController coursesController;

    @BeforeEach
    void setUp() {
        mockMvc = MockMvcBuilders.standaloneSetup(coursesController).build();
    }

    @Nested
    class getCoursesForSeason {
        @Test
        @DisplayName("When a season is requested, the course list for that season is returned")
        void ok() throws Exception {
            when(mockCoursesService.getCourseList("2022")).thenReturn("courses list");

            mockMvc.perform(get("/courses/2022"))
                    .andExpect(status().isOk())
                    .andExpect(content().contentType(MediaType.TEXT_PLAIN + ";charset=ISO-8859-1"))
                    .andExpect(MockMvcResultMatchers.content().string("courses list"));
        }
    }
}