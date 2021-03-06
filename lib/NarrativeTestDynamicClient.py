# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class NarrativeTestDynamic(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def sample_dyn_service_call(self, params, context=None):
        """
        A simple loopback function. The single string input is just returned as output. Useful for
        testing clients that talk to dynamic services.
        :param params: instance of type "SampleCallParams" -> structure:
           parameter "input" of String
        :returns: instance of type "SampleCallResult" -> structure: parameter
           "output" of String
        """
        return self._client.call_method(
            'NarrativeTestDynamic.sample_dyn_service_call',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('NarrativeTestDynamic.status',
                                        [], self._service_ver, context)
