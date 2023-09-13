package com.example.example_maven_springboot_fullstack.drivers;

import com.example.example_maven_springboot_fullstack.ergast.ErgastClient;
import com.example.example_maven_springboot_fullstack.rapid.RapidClient;
import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Service
public class DriversService
{
    private ErgastClient ergastClient;
    private RapidClient rapidClient;
    private DriverRepo driverRepo;

    public DriversService(DriverRepo driverRepo, ErgastClient ergastClient, RapidClient rapidClient) {
        this.ergastClient = ergastClient;
        this.driverRepo = driverRepo;
        this.rapidClient = rapidClient;

    }
    private static final Gson gson = new Gson();
    public ArrayList<Driver> getDriversList() {

        ArrayList<Driver> driverList = (ArrayList<Driver>) driverRepo.findAll();
        for (Driver driver : driverList) {
            System.out.println("Recalling driver: " + driver.getGivenName());
        }
        return driverList;
    }

    public void refreshDriversRepo()
    {
        ArrayList<Driver> driverList;
        driverList = null;
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

    public String getDriver(String name) {
        Driver driverJson = driverRepo.findByGivenName(name);
        String payloadStr = gson.toJson(driverJson);
        System.out.println("Found driver : " + payloadStr);
        return (driverJson == null ? String.format("None Found for: %s", name) : payloadStr);
    }

    public String getRapidDriver(String name) {
        rapidClient.getDriverByName(name);
        return "test";
    }
}
