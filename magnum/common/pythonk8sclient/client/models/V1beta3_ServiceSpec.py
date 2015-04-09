#!/usr/bin/env python
"""
Copyright 2015 Reverb Technologies, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

class V1beta3_ServiceSpec(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'createExternalLoadBalancer': 'bool',
            
            
            'portalIP': 'str',
            
            
            'ports': 'list[v1beta3_ServicePort]',
            
            
            'publicIPs': 'list[str]',
            
            
            'selector': 'any',
            
            
            'sessionAffinity': 'str'
            
        }

        self.attributeMap = {
            
            'createExternalLoadBalancer': 'createExternalLoadBalancer',
            
            'portalIP': 'portalIP',
            
            'ports': 'ports',
            
            'publicIPs': 'publicIPs',
            
            'selector': 'selector',
            
            'sessionAffinity': 'sessionAffinity'
            
        }       

        
        #set up a cloud-provider-specific load balancer on an external IP
        
        self.createExternalLoadBalancer = None # bool
        
        
        self.portalIP = None # str
        
        #ports exposed by the service
        
        self.ports = None # list[v1beta3_ServicePort]
        
        #externally visible IPs (e.g. load balancers) that should be proxied to this service
        
        self.publicIPs = None # list[str]
        
        #label keys and values that must match in order to receive traffic for this service; if empty, all pods are selected, if not specified, endpoints must be manually specified
        
        self.selector = None # any
        
        #enable client IP based session affinity; must be ClientIP or None; defaults to None
        
        self.sessionAffinity = None # str
        
