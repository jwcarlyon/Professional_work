package com.example.example_maven_springboot_fullstack.drivers;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
@RequestMapping(path = "/drivers")
public class DriversController
{
//    private Logger logger = new Logger();
    private DriversService driversService;
    public DriversController(DriversService driversService) {
        this.driversService = driversService;
    }
    @RequestMapping(path = "/welcome")
    public String helloWorld()
    {
        String message = "<h3>Hello F1 World!</h3>";
        return message;
    }
    @RequestMapping(path = "/refresh")
    public String refreshDriversList()
    {

        driversService.refreshDriversRepo();
        String message = "Drivers list successfully updated";
        return message;
    }
    @RequestMapping(path = "/all-drivers")
    public ResponseEntity<ArrayList<Driver>> getDriversList()
    {
        ArrayList<Driver> driverList = driversService.getDriversList();
        return new ResponseEntity<>(driverList, HttpStatus.OK);
    }
    @RequestMapping(path = "/{name}")
    public ResponseEntity<String> getDriverByName(@PathVariable String name)
    {
        String driver = driversService.getDriver(name);
        return new ResponseEntity<>(driver, HttpStatus.OK);
    }
}
