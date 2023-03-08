package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.drivers.Driver;
import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.Map;

@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({ "season", "Drivers" })
public class DriverTable {
    @JsonProperty("season")
    private String season;
    @JsonProperty("Drivers")
    private Driver[] drivers;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("season")
    public String getSeason() {
        return season;
    }

    @JsonProperty("season")
    public void setSeason(String season) {
        this.season = season;
    }

    @JsonProperty("Drivers")
    public Driver[] getDrivers() {
        return drivers;
    }

    @JsonProperty("Drivers")
    public void setDrivers(Driver[] drivers) {
        this.drivers = drivers;
    }
    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }
}
