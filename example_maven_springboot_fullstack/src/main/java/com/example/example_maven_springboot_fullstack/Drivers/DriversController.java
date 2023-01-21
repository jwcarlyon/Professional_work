package com.example.example_maven_springboot_fullstack.Drivers;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

@RestController
@RequestMapping(path = "/drivers")
public class DriversController
{
    @RequestMapping(path = "/welcome")
    public String helloWorld()
    {
        String message = "<h3>Hello F1 World!</h3>";
        return message;
    }
}
