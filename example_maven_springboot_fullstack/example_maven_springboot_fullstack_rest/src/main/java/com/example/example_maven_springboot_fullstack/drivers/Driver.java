package com.example.example_maven_springboot_fullstack.drivers;

import com.fasterxml.jackson.annotation.JsonAlias;
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
        @JsonAlias({ "driverId", "driverId" })
        private String driverId;
        @Column
        @JsonAlias({ "permanent_number", "permanentNumber" })
        private Integer permanentNumber;
        @Column
        @JsonProperty("code")
        private String code;
        @Column
        @JsonProperty("url")
        private String url;
        @Column
        @JsonAlias({ "given_name", "givenName" })
        private String givenName;
        @Column
        @JsonAlias({ "family_name", "familyName" })
        private String familyName;
        @Column
        @JsonAlias({ "date_of_birth", "dateOfBirth" })
        private String dateOfBirth;// "1981-07-29"
        @Column
        @JsonProperty("nationality")
        private String nationality;
}
