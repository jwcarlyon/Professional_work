package com.example.example_maven_springboot_fullstack.config;

import org.springframework.web.context.WebApplicationContext;
import org.springframework.web.context.support.AnnotationConfigWebApplicationContext;
import org.springframework.web.servlet.support.AbstractDispatcherServletInitializer;

public class AnnotationsBasedApplicationAndServletInitializer
  extends AbstractDispatcherServletInitializer
{
    @Override
    protected WebApplicationContext createRootApplicationContext()
    {
        AnnotationConfigWebApplicationContext rootContext
          = new AnnotationConfigWebApplicationContext();
        rootContext.register(RootApplicationConfig.class);
        return rootContext;
    }
    @Override
    protected WebApplicationContext createServletApplicationContext()
    {
        AnnotationConfigWebApplicationContext normalWebAppContext
          = new AnnotationConfigWebApplicationContext();
        normalWebAppContext.register(RootApplicationConfig.class);
        return normalWebAppContext;
    }
    // AbstractDispatcherServletInitializer <--------------------------------
    // That's an abstract class that, besides creating a root web application
    // context as previously seen, allows us to register one dispatcher servlet
    // with minimum boilerplate:
    @Override
    protected String[] getServletMappings()
    {
        return new String[] { "/api/*" };
    }
    @Override
    protected String getServletName()
    {
        return "normal-dispatcher";
    }
}
