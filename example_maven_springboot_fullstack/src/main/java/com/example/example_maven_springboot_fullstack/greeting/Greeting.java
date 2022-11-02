package com.example.example_maven_springboot_fullstack.greeting;

public class Greeting
{
    private String message;

    public String getMessage()
    {
        return message;
    }

    public void setMessage(String message)
    {
        this.message = message;
    }

    @Override
    public String toString()
    {
        return "Greeting [message=" + message + "]";
    }
}
