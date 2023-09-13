package com.example.example_maven_springboot_fullstack.drivers;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.repository.query.Param;


public interface DriverRepo extends JpaRepository<Driver, Integer> {
//    @Query("SELECT d FROM Driver d WHERE d.givenName = ':name'")
    Driver findByGivenName(@Param("name") String name);

}
