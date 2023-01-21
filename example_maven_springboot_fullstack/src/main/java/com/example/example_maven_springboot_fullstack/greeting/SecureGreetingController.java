package com.example.example_maven_springboot_fullstack.greeting;

import com.example.example_maven_springboot_fullstack.config.ApplicationContextUtilService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.ApplicationContext;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.context.ContextLoader;
import org.springframework.web.context.WebApplicationContext;

import java.util.Arrays;

@Controller
public class SecureGreetingController
{

    @Autowired
    WebApplicationContext webApplicationContext;

    @Autowired
    private GreeterService greeterService;

    @Autowired
    @Qualifier("contextAware")
    private ApplicationContextUtilService contextUtilService;

    @RequestMapping(path = "/secure-welcome")
    public String helloWorld()
    {
        processContext();
        String message = "<br><div style='text-align:center;'>" + "<h3>Secure " + greeterService.greet() + "</h3></div>";
        return message;
    }

    private void processContext()
    {
        ApplicationContext context = contextUtilService.getApplicationContext();
        System.out.println("application context : " + context);
        if(context.getBeanDefinitionNames() != null)
        {
            System.out.println("application context Beans: " + Arrays.asList(context.getBeanDefinitionNames()));
        }
        WebApplicationContext rootContext = ContextLoader.getCurrentWebApplicationContext();
        System.out.println("root context is not visible: " + rootContext);

        System.out.println("web context : " + webApplicationContext);
        if(webApplicationContext.getBeanDefinitionNames() != null)
        {
            System.out.println("web context Beans: " + Arrays.asList(webApplicationContext.getBeanDefinitionNames()));
        }
    }
}
