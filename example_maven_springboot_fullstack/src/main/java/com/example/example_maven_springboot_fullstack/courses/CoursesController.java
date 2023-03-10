package com.example.example_maven_springboot_fullstack.courses;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/courses")
public class CoursesController {
    private CoursesService coursesService;

    public CoursesController(CoursesService coursesService) {
        this.coursesService = coursesService;
    }

    @RequestMapping(path = "/{season}", method = RequestMethod.GET)
    public ResponseEntity<String> getCoursesForSeason(@PathVariable String season) {
        return new ResponseEntity<>(coursesService.getCourseList(season), HttpStatus.OK);
    }
}
