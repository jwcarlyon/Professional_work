package com.example.example_maven_springboot_fullstack.drivers;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;


public interface DriverRepo extends JpaRepository<Driver, Integer> {
    Driver findByGivenName(@Param("name") String name);

}
