package com.example.example_maven_springboot_fullstack.Drivers;

import org.springframework.data.jpa.repository.JpaRepository;


public interface DriverRepo extends JpaRepository<Driver, Integer> {
}
