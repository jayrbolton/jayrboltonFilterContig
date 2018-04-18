
package us.kbase.jayrboltoncontigfilter;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: ContigFilterResults</p>
 * <pre>
 * Output results
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "report_name",
    "report_ref",
    "filtered_assembly_ref",
    "n_total",
    "n_remaining"
})
public class ContigFilterResults {

    @JsonProperty("report_name")
    private String reportName;
    @JsonProperty("report_ref")
    private String reportRef;
    @JsonProperty("filtered_assembly_ref")
    private String filteredAssemblyRef;
    @JsonProperty("n_total")
    private Long nTotal;
    @JsonProperty("n_remaining")
    private Long nRemaining;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("report_name")
    public String getReportName() {
        return reportName;
    }

    @JsonProperty("report_name")
    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public ContigFilterResults withReportName(String reportName) {
        this.reportName = reportName;
        return this;
    }

    @JsonProperty("report_ref")
    public String getReportRef() {
        return reportRef;
    }

    @JsonProperty("report_ref")
    public void setReportRef(String reportRef) {
        this.reportRef = reportRef;
    }

    public ContigFilterResults withReportRef(String reportRef) {
        this.reportRef = reportRef;
        return this;
    }

    @JsonProperty("filtered_assembly_ref")
    public String getFilteredAssemblyRef() {
        return filteredAssemblyRef;
    }

    @JsonProperty("filtered_assembly_ref")
    public void setFilteredAssemblyRef(String filteredAssemblyRef) {
        this.filteredAssemblyRef = filteredAssemblyRef;
    }

    public ContigFilterResults withFilteredAssemblyRef(String filteredAssemblyRef) {
        this.filteredAssemblyRef = filteredAssemblyRef;
        return this;
    }

    @JsonProperty("n_total")
    public Long getNTotal() {
        return nTotal;
    }

    @JsonProperty("n_total")
    public void setNTotal(Long nTotal) {
        this.nTotal = nTotal;
    }

    public ContigFilterResults withNTotal(Long nTotal) {
        this.nTotal = nTotal;
        return this;
    }

    @JsonProperty("n_remaining")
    public Long getNRemaining() {
        return nRemaining;
    }

    @JsonProperty("n_remaining")
    public void setNRemaining(Long nRemaining) {
        this.nRemaining = nRemaining;
    }

    public ContigFilterResults withNRemaining(Long nRemaining) {
        this.nRemaining = nRemaining;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((((((((("ContigFilterResults"+" [reportName=")+ reportName)+", reportRef=")+ reportRef)+", filteredAssemblyRef=")+ filteredAssemblyRef)+", nTotal=")+ nTotal)+", nRemaining=")+ nRemaining)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
