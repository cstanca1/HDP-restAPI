#Ambari and Resource Manager REST API with Python

Download and install pip
```
#wget https://bootstrap.pypa.io/get-pip.py
```
Install add-on package
```
#pip install requests
```
Start Python CLI (default version)
```
#python
```
Import pre-reqs
```
>>>import requests
```
```
>>>import json
```
```
>>>import sys
```
Set Ambari domain variable to the IP address or FQDN of your Ambari node.
```
>>>AMBARI_DOMAIN='127.0.0.1'
```
Set Ambari port, Ambari user and password variables to match your specifics. 
```
>>>AMBARI_PORT='8080'
```
```
>>>AMBARI_USER_ID='admin'
```
```
>>>AMBARI_USER_PW='admin'
```
Set the following variable to the IP address or FQDN of your ResourceManager node.
```
>>>RM_DOMAIN='127.0.0.1'
```
Set Resource Manager port variable
```
>>>RM_PORT='8088'
```
Let's find Cluster Name, Cluster Version, Stack and Stack Version:
```
>>>restAPI='/api/v1/clusters'
```
```
>>>url="http://"+AMBARI_DOMAIN+":"+AMBARI_PORT+restAPI
```
```
>>>r=requests.get(url, auth=(AMBARI_USER_ID, AMBARI_USER_PW))
```
```
>>>json_data=json.loads(r.text)
```
```
>>>CLUSTER_NAME=json_data["items"][0]["Clusters"]["cluster_name"]
```
```
>>>print(CLUSTER_NAME)
```
```
>>>CLUSTER_VERSION=json_data["items"][0]["Clusters"]["version"]
```
```
>>>print(CLUSTER_VERSION)
```
```
>>>STACK=CLUSTER_VERSION.split('-')[0]
```
```
>>>print(STACK)
```
```
>>>STACK_VERSION = CLUSTER_VERSION.split('-')[1]
```
```
>>>print(STACK_VERSION)
```
```
>>>CLUSTER_INFO=json_data
```
```
>>>print(CLUSTER_INFO)
```
Let's find HDP stack repository:
```
>>>restAPI="/api/v1/stacks/"+STACK+"/versions/"+STACK_VERSION+"/operating_systems/redhat7/repositories/"+CLUSTER_VERSION
```
```
>>>url="http://"+AMBARI_DOMAIN+":"+AMBARI_PORT+restAPI
```
```
>>>r=requests.get(url, auth=(AMBARI_USER_ID, AMBARI_USER_PW))
```
```
>>>json_data=json.loads(r.text)
```
```
>>>print(json_data)
```
```
>>>REPOSITORY_NAME=json_data["Repositories"]["latest_base_url"]
```
```
>>>print(REPOSITORY_NAME)
```
A more elegant approach is to create utility functions. See restAPIFunctions.py script.
For example, CLUSTER_VERSION and CLUSTER_NAME can be found using getClusterVersionAndName() function:
```
>>>>CLUSTER_NAME,CLUSTER_VERSION,CLUSTER_INFO = getClusterVersionAndName()
>>>>print(CLUSTER_NAME)
>>>>print(CLUSTER_VERSION)
>>>>print(CLUSTER_INFO)
```
```
