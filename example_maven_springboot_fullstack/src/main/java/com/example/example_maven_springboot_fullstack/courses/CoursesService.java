package com.example.example_maven_springboot_fullstack.courses;

import com.example.example_maven_springboot_fullstack.ergast.ErgastClient;
import org.springframework.stereotype.Service;

@Service
public class CoursesService {
    private ErgastClient ergastClient;

    public CoursesService(ErgastClient ergastClient) {
        this.ergastClient = ergastClient;
    }

    public String getCourseList(String season) {
        return ergastClient.getAllCoursesBySeason(season);
    }
}
