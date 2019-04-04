# -*- coding: utf-8 -*-
#BEGIN_HEADER
# The header block is where all import statments should live
import logging
import os
from pprint import pformat

from Bio import SeqIO

from installed_clients.AssemblyUtilClient import AssemblyUtil
from installed_clients.KBaseReportClient import KBaseReport
#END_HEADER


class NarrativeTestDynamic:
    '''
    Module Name:
    NarrativeTestDynamic

    Module Description:
    A KBase module: NarrativeTestDynamic
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    # Class variables and functions can be defined in this block
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR

        # Any configuration parameters that are important should be parsed and
        # saved in the constructor.
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def sample_dyn_service_call(self, ctx, params):
        """
        A simple loopback function. The single string input is just returned as output. Useful for
        testing clients that talk to dynamic services.
        :param params: instance of type "SampleCallParams" -> structure:
           parameter "input" of String
        :returns: instance of type "SampleCallResult" -> structure: parameter
           "output" of String
        """
        # ctx is the context object
        # return variables are: result
        #BEGIN sample_dyn_service_call
        if "input" not in params:
            raise ValueError('Key "input" not found in parameters.')
        result = {
            "output": params["input"]
        }
        #END sample_dyn_service_call

        # At some point might do deeper type checking...
        if not isinstance(result, dict):
            raise ValueError('Method sample_dyn_service_call return value ' +
                             'result is not type dict as required.')
        # return the results
        return [result]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
