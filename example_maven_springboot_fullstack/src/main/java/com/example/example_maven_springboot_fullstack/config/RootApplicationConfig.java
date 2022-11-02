package com.example.example_maven_springboot_fullstack.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import com.example.example_maven_springboot_fullstack.greeting.Greeting;

@Configuration
@ComponentScan(basePackages = { "com.example.example_maven_springboot_fullstack.greeting" })
public class RootApplicationConfig
{
    @Bean
    public Greeting greeting()
    {
        Greeting greeting = new Greeting();
        greeting.setMessage("Hello World !!");
        return greeting;
    }
}
