package com.example.example_maven_springboot_fullstack.drivers;

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

import java.util.ArrayList;
import java.util.Arrays;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class DriversControllerTest {

    private MockMvc mockMvc;
    @Mock
    private DriversService mockDriversService;

    @InjectMocks
    private DriversController driversController;

    @BeforeEach
    void setUp() { mockMvc = MockMvcBuilders.standaloneSetup(driversController).build(); }

    @Nested
    class driversWelcome {
        @Test
        @DisplayName("When a welcome request is made, then a hello world response message is returned with a 200/OK")
        void helloWorld() throws Exception {
            mockMvc.perform(get("/drivers/welcome"))
                    .andExpect(status().isOk())
                    .andExpect(content().contentType(MediaType.TEXT_PLAIN + ";charset=ISO-8859-1"))
                    .andExpect(MockMvcResultMatchers.content().string("<h3>Hello F1 World!</h3>"));
        }
    }

    @Nested
    class driversRefresh {
        @Test
        @DisplayName("When a refresh request is made, " +
                "then the drivers repo is refreshed and a success response message is returned with a 200/OK")
        void refreshDriversList() throws Exception {
            mockMvc.perform(get("/drivers/refresh"))
                    .andExpect(status().isOk())
                    .andExpect(content().contentType(MediaType.TEXT_PLAIN + ";charset=ISO-8859-1"))
                    .andExpect(MockMvcResultMatchers.content().string("Drivers list successfully updated"));

            verify(mockDriversService).refreshDriversRepo();
        }
    }

    @Nested
    class driversName {
        @Test
        @DisplayName("When an driver request is made, then an ArrayList of stats is returned with a 200/OK")
        void getDriversList() throws Exception {
            Driver driver1 = new Driver();
            driver1.setDriverId("test1");
            when(mockDriversService.getDriver("lewis")).thenReturn(driver1.toString());

            mockMvc.perform(get("/drivers/lewis"))
                    .andExpect(status().isOk())
                    .andExpect(content().contentType(MediaType.TEXT_PLAIN + ";charset=ISO-8859-1"))
                    .andExpect(MockMvcResultMatchers.content().string(driver1.toString()));
        }
    }
    @Nested
    class driversAllDrivers {
        @Test
        @DisplayName("When an all-drivers request is made, then an ArrayList of Drivers is returned with a 200/OK")
        void getDriversList() throws Exception {
            Driver driver1 = new Driver();
            Driver driver2 = new Driver();
            driver1.setDriverId("test1");
            driver2.setDriverId("test2");
            ArrayList<Driver> expectedDriversList = new ArrayList<>(Arrays.asList(driver1, driver2));
            when(mockDriversService.getDriversList()).thenReturn(expectedDriversList);

            mockMvc.perform(get("/drivers/all-drivers"))
                    .andExpect(status().isOk())
                            .andExpect(content().contentType(MediaType.APPLICATION_JSON_VALUE))
                    .andExpect(MockMvcResultMatchers.jsonPath("$[0].driverId").value(driver1.getDriverId()))
                    .andExpect(MockMvcResultMatchers.jsonPath("$[1].driverId").value(driver2.getDriverId()));
        }
    }
}