/*
A KBase module: jayrboltonContigFilter
*/

module jayrboltonContigFilter {
    /* Input parameters */
    typedef structure {
        int min_length;
        string assembly_ref;
    } ContigFilterParams;

    /* Output results */
    typedef structure {
        string report_name;
        string report_ref;
        string filtered_assembly_ref;
        int n_total;
        int n_remaining;
    } ContigFilterResults;

    funcdef filter_contigs(string workspace_name, ContigFilterParams params)
        returns (ContigFilterResults) authentication required;
};
