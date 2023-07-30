package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.courses.GpLapTime;
import com.fasterxml.jackson.annotation.*;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.HashMap;
import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({"season", "round", "Races"})
public class RaceTable {
    @JsonProperty("season")
    private String season;
    @JsonProperty("round")
    private String round;
    @JsonProperty("Races")
    private Race[] races;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<>();

    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonPropertyOrder({"season", "round", "url", "raceName", "Circuit"})
    public class Race {
        @JsonProperty("season")
        private String season;
        @JsonProperty("round")
        private String round;
        @JsonProperty("url")
        private String url;
        @JsonProperty("raceName")
        private String raceName;
        @JsonProperty("Circuit")
        private Circuit circuit;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonPropertyOrder({"circuitId", "url", "round", "circuitName", "Location", "date", "time", "Laps" })
    public class Circuit {
        @JsonProperty("circuitId")
        private String circuitId;
        @JsonProperty("url")
        private String url;
        @JsonProperty("round")
        private String round;
        @JsonProperty("circuitName")
        private String circuitName;
        @JsonProperty("Location")
        private Location location;
        @JsonProperty("date")
        private String date;
        @JsonProperty("time")
        private String time;
        @JsonProperty("Laps")
        private GpLapTime[] laps;
    }

    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonPropertyOrder({"lat", "long", "locality", "country"})
    public class Location {
        @JsonProperty("lat")
        private String latitude;
        @JsonProperty("long")
        private String longitude;
        @JsonProperty("locality")
        private String locality;
        @JsonProperty("country")
        private String country;
        @JsonProperty("Location")
        private Location location;
    }
}
