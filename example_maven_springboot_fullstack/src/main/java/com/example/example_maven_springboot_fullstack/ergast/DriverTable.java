package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.drivers.Driver;
import com.fasterxml.jackson.annotation.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.util.HashMap;
import java.util.Map;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({ "season", "Drivers" })
public class DriverTable {
    @JsonProperty("season")
    private String season;
    @JsonProperty("Drivers")
    private Driver[] drivers;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }
}
