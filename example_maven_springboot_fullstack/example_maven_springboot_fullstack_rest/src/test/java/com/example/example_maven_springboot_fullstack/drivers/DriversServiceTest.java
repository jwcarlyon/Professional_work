package com.example.example_maven_springboot_fullstack.drivers;

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
import java.util.Arrays;

import static org.junit.jupiter.api.Assertions.assertAll;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.ArgumentMatchers.anyString;
import static org.mockito.Mockito.*;

@ExtendWith(SpringExtension.class)
@ExtendWith(MockitoExtension.class)
class DriversServiceTest {

    @Mock
    private DriverRepo mockDriverRepo;
    @Mock
    private ErgastClient mockErgastClient;
    @InjectMocks
    private DriversService driversService;

    @Nested
    class driversService {
        @Test
        @DisplayName("When repo returns all drivers, then an ArrayList type is returned")
        void getDriversList() {
            Driver driver1 = new Driver();
            Driver driver2 = new Driver();
            ArrayList<Driver> expectedDriversList = new ArrayList<>(Arrays.asList(driver1, driver2));
            when(mockDriverRepo.findAll()).thenReturn(expectedDriversList);

            ArrayList<Driver> result = driversService.getDriversList();

            assertAll("all drivers are present",
                    () -> assertEquals(driver1, result.get(0)),
                    () -> assertEquals(driver2, result.get(1))
            );
        }

        @Test
        @DisplayName("When ergast client returns driver list, " +
                "then an equivalent ArrayList type is iteratively saved to repo")
        void refreshDriversRepo() throws Exception {
            Driver driver1 = new Driver();
            Driver driver2 = new Driver();
            Driver[] expectedDriverArray = new Driver[] { driver1, driver2 };
            when(mockErgastClient.getAllDriversByYear(anyString())).thenReturn(expectedDriverArray);

            driversService.refreshDriversRepo();

            verify(mockDriverRepo).save(driver1);
            verify(mockDriverRepo).save(driver2);
            verifyNoMoreInteractions(mockDriverRepo);
        }
    }
}