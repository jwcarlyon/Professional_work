package com.example.example_maven_springboot_fullstack.Ergast;

import com.example.example_maven_springboot_fullstack.Drivers.Driver;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.io.IOException;
import java.util.List;

@Service
public class ErgastClient {
    @Autowired
    private RestTemplate ergastAPI;

    public ErgastClient(RestTemplate ergastAPI) {
        this.ergastAPI = ergastAPI;
    }

    public Driver[] getAllDriversByYear(String year) throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        String response = ergastAPI.getForObject(String.format("http://ergast.com/api/f1/%s/drivers.json", year), String.class);
        System.out.println("Converting Ergast response : " + response);
        ErgastResponseDriversList ergastResponseDriversList = mapper.readValue(response, ErgastResponseDriversList.class);
        MRData mrData = ergastResponseDriversList.getMrData();
        DriverTable driverTable = mrData.getDriverTable();
        Driver[] drivers = driverTable.getDrivers();//        System.out.println("Received Ergast response : " + response);
        List<Driver> cars = List.of(driverTable.getDrivers());
        for(Driver car : cars) {
            System.out.println(car.getDriverId());
        }
//        Gson gson = new GsonBuilder().create();
//        Driver[] drivers = gson.fromJson(response.substring(response.indexOf('['), response.indexOf(']') + 1), Driver[].class);
//        return gson.fromJson(response.substring(response.indexOf('['), response.indexOf(']') + 1), Driver[].class);
        return drivers;
    }
}
