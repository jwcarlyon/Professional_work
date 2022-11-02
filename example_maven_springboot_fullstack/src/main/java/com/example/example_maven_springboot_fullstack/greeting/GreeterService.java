package com.example.example_maven_springboot_fullstack.greeting;

import javax.annotation.Resource;

import org.springframework.stereotype.Service;

@Service
public class GreeterService
{
    @Resource
    private Greeting greeting;

    public String greet()
    {
        return greeting.getMessage();
    }
}
