package com.example.example_maven_springboot_fullstack.greeting;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class GreetingController {
    @Autowired
    private GreeterService greeterService;

    @RequestMapping(path = "/welcome")
    public ModelAndView helloWorld()
    {
        String message = "<h3>Normal " + greeterService.greet() + "</h3>";
        return new ModelAndView("welcome", "message", message);
    }
}
