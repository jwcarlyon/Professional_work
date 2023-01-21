package com.example.example_maven_springboot_fullstack.greeting;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
    @Autowired
    private GreeterService greeterService;

    @RequestMapping(path = "/welcome")
    public String helloWorld()
    {
        String message = "<h3>Normal " + greeterService.greet() + "</h3>";
        return message;
    }
}
