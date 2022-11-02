package com.example.example_maven_springboot_fullstack.course;

import java.net.URI;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

@RestController
public class CourseController
{
  	@Autowired
  	private CourseService courseService;

    // @Autowired
    // @Qualifier("contextAware")
    // private ApplicationContextUtilService contextUtilService;

    @GetMapping("/instructors/{username}/courses")
  	public List<Course> getAllCourses(@PathVariable String username)
    {
  		  return courseService.findAll();
  	}

  	@GetMapping("/instructors/{username}/courses/{id}")
  	public Course getCourse(@PathVariable String username, @PathVariable long id)
    {
  		  return courseService.findById(id);
  	}

  	@DeleteMapping("/instructors/{username}/courses/{id}")
  	public ResponseEntity<Void> deleteCourse(@PathVariable String username, @PathVariable long id)
    {
    		Course course = courseService.deleteById(id);
    		if (course != null)
        {
    			return ResponseEntity.noContent().build();
    		}
    		return ResponseEntity.notFound().build();
  	}

  	@PutMapping("/instructors/{username}/courses/{id}")
  	public ResponseEntity<Course> updateCourse(@PathVariable String username, @PathVariable long id,
  			@RequestBody Course course)
    {
    		Course courseUpdated = courseService.save(course);
    		return new ResponseEntity<Course>(course, HttpStatus.OK);
  	}

  	@PostMapping("/instructors/{username}/courses")
  	public ResponseEntity<Void> createCourse(@PathVariable String username, @RequestBody Course course)
    {
    		Course createdCourse = courseService.save(course);
    		// Location
    		// Get current resource url
    		/// {id}
    		URI uri = ServletUriComponentsBuilder
          .fromCurrentRequest()
          .path("/{id}")
          .buildAndExpand(createdCourse.getId())
    			.toUri();
    		return ResponseEntity.created(uri).build();
  	}
}
