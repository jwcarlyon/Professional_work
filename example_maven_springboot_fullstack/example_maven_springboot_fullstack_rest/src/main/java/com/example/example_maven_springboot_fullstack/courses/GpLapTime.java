package com.example.example_maven_springboot_fullstack.courses;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({ "driverId", "permanentNumber", "code", "url", "givenName", "familyName", "dateOfBirth", "nationality" })
public class GpLapTime {
    @Id
    @GeneratedValue(strategy=GenerationType.IDENTITY)
    private Integer mysql_id;
    @Column
    @JsonProperty("driverId")
    private String driverId;

    @Column
    @JsonProperty("position")
    private String position;

    @Column
    @JsonProperty("time")
    private String time;
}
