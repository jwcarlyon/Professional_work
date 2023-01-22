package com.example.example_maven_springboot_fullstack.Ergast;

import com.fasterxml.jackson.annotation.*;

import java.util.HashMap;
import java.util.Map;

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
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("xmlns")
    public String getXmlns() { return this.xmlns; }

    @JsonProperty("xmlns")
    public void setXmlns(String xmlns) {
        this.xmlns = xmlns;
    }

    @JsonProperty("series")
    public String getSeries() {
        return series;
    }

    @JsonProperty("series")
    public void setSeries(String series) {
        this.series = series;
    }
    @JsonProperty("url")
    public String getUrl() { return this.url; }

    @JsonProperty("url")
    public void setUrl(String url) {
        this.url = url;
    }

    @JsonProperty("limit")
    public Integer getLimit() {
        return limit;
    }

    @JsonProperty("limit")
    public void setLimit(Integer limit) {
        this.limit = limit;
    }

    @JsonProperty("offset")
    public Integer getOffset() {
        return offset;
    }

    @JsonProperty("offset")
    public void setOffset(Integer offset) {
        this.offset = offset;
    }

    @JsonProperty("total")
    public Integer getTotal() {
        return total;
    }

    @JsonProperty("total")
    public void setTotal(Integer total) {
        this.total = total;
    }

    @JsonProperty("DriverTable")
    public DriverTable getDriverTable() {
        return driverTable;
    }

    @JsonProperty("DriverTable")
    public void setDriverTable(DriverTable driverTable) {
        this.driverTable = driverTable;
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
