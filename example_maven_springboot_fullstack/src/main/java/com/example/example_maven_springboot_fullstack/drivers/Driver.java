package com.example.example_maven_springboot_fullstack.drivers;

import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;

import javax.persistence.*;

@Entity
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

        public Integer getMysql_id() {
                return mysql_id;
        }

        public void setMysql_id(Integer mysql_id) {
                this.mysql_id = mysql_id;
        }

        @JsonProperty("driverId")
        public String getDriverId() {
                return driverId;
        }

        @JsonProperty("driverId")
        public void setDriverId(String driverId) {
                this.driverId = driverId;
        }

        @JsonProperty("permanentNumber")
        public Integer getPermanentNumber() {
                return permanentNumber;
        }

        @JsonProperty("permanentNumber")
        public void setPermanentNumber(Integer permanentNumber) {
                this.permanentNumber = permanentNumber;
        }

        @JsonProperty("code")
        public String getCode() {
                return code;
        }

        @JsonProperty("code")
        public void setCode(String code) {
                this.code = code;
        }

        @JsonProperty("url")
        public String getUrl() {
                return url;
        }

        @JsonProperty("url")
        public void setUrl(String url) {
                this.url = url;
        }

        @JsonProperty("givenName")
        public String getGivenName() {
                return givenName;
        }

        @JsonProperty("givenName")
        public void setGivenName(String givenName) {
                this.givenName = givenName;
        }

        @JsonProperty("familyName")
        public String getFamilyName() {
                return familyName;
        }

        @JsonProperty("familyName")
        public void setFamilyName(String familyName) {
                this.familyName = familyName;
        }

        @JsonProperty("dateOfBirth")
        public String getDateOfBirth() {
                return dateOfBirth;
        }

        @JsonProperty("dateOfBirth")
        public void setDateOfBirth(String dateOfBirth) {
                this.dateOfBirth = dateOfBirth;
        }

        @JsonProperty("nationality")
        public String getNationality() {
                return nationality;
        }

        @JsonProperty("nationality")
        public void setNationality(String nationality) {
                this.nationality = nationality;
        }
}
