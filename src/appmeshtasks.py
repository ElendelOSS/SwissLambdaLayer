import json
import logging
from appmesh import appmesh

from botocore.exceptions import ClientError


class appmeshtasks:
    def __init__(self, region):
        self.appmeshtasks = appmesh(region)

    def build_spec(self):
        spec = {
            'httpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                },
                'match': {
                    'prefix': 'string'
                }
            },
            'tcpRoute': {
                'action': {
                    'weightedTargets': [
                        {
                            'virtualNode': 'string',
                            'weight': 123
                        },
                    ]
                }
            }
        }

        return spec

    def build_spec_backends(self):
        backends = [
            {
                'virtualService': {
                    'virtualServiceName': 'string'
                }
            },
        ]

        return backends

    def build_spec_listeners(self):
        listeners = [
            {
                'healthCheck': {
                    'healthyThreshold': 123,
                    'intervalMillis': 123,
                    'path': 'string',
                    'port': 123,
                    'protocol': 'http'|'tcp',
                    'timeoutMillis': 123,
                    'unhealthyThreshold': 123
                },
                'portMapping': {
                    'port': 123,
                    'protocol': 'http'|'tcp'
                }
            },
        ]

        return listeners

    def build_spec_loggers(self):
        logging = {
            'accessLog': {
                'file': {
                    'path': 'string'
                }
            }
        }

        return logging

    def build_spec_service_discovery(self):
        service_discovery = {
            'awsCloudMap': {
                'attributes': [
                    {
                        'key': 'string',
                        'value': 'string'
                    },
                ],
                'namespaceName': 'string',
                'serviceName': 'string'
            },
            'dns': {
                'hostname': 'string'
            }
        }

        return service_discovery

    