/*
A KBase module: jayrboltonContigFilter
*/

module jayrboltonContigFilter {
    /* Input parameters */
    typedef structure {
        string assembly_ref;
        string workspace_name;
        int min_length;
    } ContigFilterParams;

    /* Output results */
    typedef structure {
        string report_name;
        string report_ref;
        string filtered_assembly_ref;
        int n_total;
        int n_remaining;
    } ContigFilterResults;

    funcdef filter_contigs(ContigFilterParams params)
        returns (ContigFilterResults) authentication required;
};
