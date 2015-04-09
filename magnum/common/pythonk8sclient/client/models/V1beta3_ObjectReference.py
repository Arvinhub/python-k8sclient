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

class V1beta3_ObjectReference(object):
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        """
        Attributes:
          swaggerTypes (dict): The key is attribute name and the value is attribute type.
          attributeMap (dict): The key is attribute name and the value is json key in definition.
        """
        self.swaggerTypes = {
            
            'apiVersion': 'str',
            
            
            'fieldPath': 'str',
            
            
            'kind': 'str',
            
            
            'name': 'str',
            
            
            'namespace': 'str',
            
            
            'resourceVersion': 'str',
            
            
            'uid': 'str'
            
        }

        self.attributeMap = {
            
            'apiVersion': 'apiVersion',
            
            'fieldPath': 'fieldPath',
            
            'kind': 'kind',
            
            'name': 'name',
            
            'namespace': 'namespace',
            
            'resourceVersion': 'resourceVersion',
            
            'uid': 'uid'
            
        }       

        
        #API version of the referent
        
        self.apiVersion = None # str
        
        #if referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]
        
        self.fieldPath = None # str
        
        #kind of the referent
        
        self.kind = None # str
        
        #name of the referent
        
        self.name = None # str
        
        #namespace of the referent
        
        self.namespace = None # str
        
        #specific resourceVersion to which this reference is made, if any: https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/api-conventions.md#concurrency-control-and-consistency
        
        self.resourceVersion = None # str
        
        #uid of the referent
        
        self.uid = None # str
        
