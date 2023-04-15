package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.courses.GpLapTime;
import com.example.example_maven_springboot_fullstack.drivers.Driver;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

@Service
public class ErgastClient {
    @Autowired
    private RestTemplate ergastAPI;

    public ErgastClient(RestTemplate ergastAPI) {
        this.ergastAPI = ergastAPI;
    }

    public Driver[] getAllDriversByYear(String year) throws IOException {
        String response = ergastAPI.getForObject(String.format("http://ergast.com/api/f1/%s/drivers.json", year), String.class);
        System.out.println("Converting Ergast response : " + response);
        ObjectMapper mapper = new ObjectMapper();
        ErgastResponseDriversList ergastResponseDriversList = mapper.readValue(response, ErgastResponseDriversList.class);
        ErgastResponseDriversList.MRData mrData = ergastResponseDriversList.getMrData();
        ErgastResponseDriversList.DriverTable driverTable = mrData.getDriverTable();
        Driver[] drivers = driverTable.getDrivers();
        List<Driver> cars = List.of(driverTable.getDrivers());
        for (Driver car : cars) {
            System.out.println(car.getDriverId());
        }
        return drivers;
    }

    public  ArrayList<GpLapTime[]> getAllLapTimesFromGp(String season, String round) {
        ArrayList<GpLapTime[]> allGpLapTimes = new ArrayList<>();
        ArrayList<Integer> laps = new ArrayList<>(
                IntStream.iterate(1, i -> i + 1)
                        .limit(57).boxed()
                        .collect(Collectors.toList()));
        for (Integer lap : laps) {
            String response = ergastAPI.getForObject(String.format("http://ergast.com/api/f1/%s/%s/laps/%s.json", season, round, lap), String.class);
            System.out.println("Logging Ergast response: " + response);
            ObjectMapper mapper = new ObjectMapper();
            ErgastResponseGpLapTimeList ergastResponseGpLapTimeList;
            try {
                ergastResponseGpLapTimeList = mapper.readValue(response, ErgastResponseGpLapTimeList.class);
            } catch (JsonProcessingException | IllegalArgumentException exception) {
                System.out.println("Error reading lap times for lap: " + lap + " " + exception);
                continue;
            }
            GpLapTime[] gpLapTimes = ergastResponseGpLapTimeList.getMrData().getRaceTable().getRaces()[0].getCircuit().getLaps();
            allGpLapTimes.add(gpLapTimes);
        }
        return allGpLapTimes;
    }
}
