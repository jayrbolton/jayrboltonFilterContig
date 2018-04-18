
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
 * <p>Original spec-file type: ContigFilterParams</p>
 * <pre>
 * Input parameters
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "min_length",
    "assembly_ref"
})
public class ContigFilterParams {

    @JsonProperty("min_length")
    private Long minLength;
    @JsonProperty("assembly_ref")
    private String assemblyRef;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("min_length")
    public Long getMinLength() {
        return minLength;
    }

    @JsonProperty("min_length")
    public void setMinLength(Long minLength) {
        this.minLength = minLength;
    }

    public ContigFilterParams withMinLength(Long minLength) {
        this.minLength = minLength;
        return this;
    }

    @JsonProperty("assembly_ref")
    public String getAssemblyRef() {
        return assemblyRef;
    }

    @JsonProperty("assembly_ref")
    public void setAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
    }

    public ContigFilterParams withAssemblyRef(String assemblyRef) {
        this.assemblyRef = assemblyRef;
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
        return ((((((("ContigFilterParams"+" [minLength=")+ minLength)+", assemblyRef=")+ assemblyRef)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
