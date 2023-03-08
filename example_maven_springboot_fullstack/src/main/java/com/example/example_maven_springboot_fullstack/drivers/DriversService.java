package com.example.example_maven_springboot_fullstack.drivers;

import com.example.example_maven_springboot_fullstack.ergast.ErgastClient;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
public class DriversService
{
    private ErgastClient ergastClient;
    private DriverRepo driverRepo;

    public DriversService(DriverRepo driverRepo, ErgastClient ergastClient) {
        this.ergastClient = ergastClient;
        this.driverRepo = driverRepo;
    }
    public ArrayList<Driver> getDriversList() {

        ArrayList<Driver> driverList = (ArrayList<Driver>) driverRepo.findAll();
        for (Driver driver : driverList) {
            System.out.println("Recalling driver: " + driver.getGivenName());
        }
        return driverList;
    }

    public void refreshDriversRepo()
    {
        ArrayList<Driver> driverList = null;
        try {
            driverList = new ArrayList<>(List.of(ergastClient.getAllDriversByYear("2022")));
        } catch (IOException exception) {
            System.out.println("Failed to collect driver list: " + exception);
        }
        for (Driver driver : driverList) {
            System.out.println("Saving driver: " + driver.getGivenName());
            driverRepo.save(driver);
        }
    }
}
