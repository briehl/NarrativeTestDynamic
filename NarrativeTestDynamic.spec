/*
A KBase module: NarrativeTestDynamic
*/

module NarrativeTestDynamic {

    typedef structure {
        string input;
    } SampleCallParams;

    typedef structure {
        string output;
    } SampleCallResult;

    /*
      A simple loopback function. The single string input is just returned as output. Useful for
      testing clients that talk to dynamic services.
    */
    funcdef sample_dyn_service_call(SampleCallParams params) returns (SampleCallResult result);

};
