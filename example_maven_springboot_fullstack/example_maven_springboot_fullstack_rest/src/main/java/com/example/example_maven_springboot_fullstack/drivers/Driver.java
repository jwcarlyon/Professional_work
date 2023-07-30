package com.example.example_maven_springboot_fullstack.drivers;

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
public class Driver
{
        @Id
        @GeneratedValue(strategy=GenerationType.IDENTITY)
        private Integer mysql_id;
        @Column
        @JsonProperty("driverId")
        private String driverId;
        @Column
        @JsonProperty("permanentNumber")
        private Integer permanentNumber;
        @Column
        @JsonProperty("code")
        private String code;
        @Column
        @JsonProperty("url")
        private String url;
        @Column
        @JsonProperty("givenName")
        private String givenName;
        @Column
        @JsonProperty("familyName")
        private String familyName;
        @Column
        @JsonProperty("dateOfBirth")
        private String dateOfBirth;// "1981-07-29"
        @Column
        @JsonProperty("nationality")
        private String nationality;
}
