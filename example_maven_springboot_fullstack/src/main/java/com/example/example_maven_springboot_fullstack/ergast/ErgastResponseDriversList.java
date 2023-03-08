package com.example.example_maven_springboot_fullstack.ergast;

import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.Map;

@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({"MRData"})
public class ErgastResponseDriversList {
    @JsonProperty("MRData")
    private MRData mrData;//"MRData":{
    @JsonIgnore
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("MRData")
    public MRData getMrData() {
        return mrData;
    }

    @JsonProperty("MRData")
    public void setMrData(MRData mrData) {
        this.mrData = mrData;
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
