package com.example.example_maven_springboot_fullstack.ergast;

import com.example.example_maven_springboot_fullstack.drivers.Driver;
import com.fasterxml.jackson.annotation.*;
import lombok.*;

import java.util.HashMap;
import java.util.Map;

@Data
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({"MRData"})
public class ErgastResponseDriversList {
    @JsonProperty("MRData")
    private MRData mrData;
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<>();
    @JsonAnySetter
    public void setAdditionalProperty(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Data
    @Getter
    @Setter
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonPropertyOrder({ "xmlns", "series", "url", "limit", "offset", "total", "DriverTable" })
    public class MRData {
        @JsonProperty("xmlns")
        private String xmlns;//":"http:\/\/ergast.com\/mrd\/1.5",
        @JsonProperty("series")
        private String series;//":"f1",
        @JsonProperty("url")
        private String url;//":"http://ergast.com/api/f1/2022/drivers.json",
        @JsonProperty("limit")
        private Integer limit;//":"30",
        @JsonProperty("offset")
        private Integer offset;//":"0",
        @JsonProperty("total")
        private Integer total;//":"22",
        @JsonProperty("DriverTable")
        private DriverTable driverTable;
        @JsonIgnore
        private Map<String, Object> additionalProperties = new HashMap<>();


        @JsonAnySetter
        public void setAdditionalProperty(String name, Object value) {
            this.additionalProperties.put(name, value);
        }
    }
    @Data
    @NoArgsConstructor
    @AllArgsConstructor
    @JsonInclude(JsonInclude.Include.NON_NULL)
    @JsonPropertyOrder({ "season", "Drivers" })
    public static class DriverTable {
        @JsonProperty("season")
        private String season;
        @JsonProperty("Drivers")
        private Driver[] drivers;
        @JsonIgnore
        private Map<String, Object> additionalProperties = new HashMap<>();

        @JsonAnySetter
        public void setAdditionalProperty(String name, Object value) {
            this.additionalProperties.put(name, value);
        }
    }
}
