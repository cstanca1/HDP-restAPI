# Ambari and Resource Manager REST API with Python

Download pip if not already in your system - you may need sudo privileges
```wget https://bootstrap.pypa.io/get-pip.py```

Install add-on package - you may need sudo privileges
```#pip install requests```

Start Python - default version
```#python```

Import a few libraries
```>>>>import requests```
```>>>>import json```
```>>>>import sys```

Set Ambari domain to the IP address of your Ambari node, or qualified node name. Below IP address is an example.
```>>>AMBARI_DOMAIN = '127.0.0.1'```

Set Ambari port, Ambari user and password. Below are just examples. 
```>>>AMBARI_PORT = '8080'```
```>>>AMBARI_USER_ID = 'admin'```
```>>>AMBARI_USER_PW = 'admin'```

Set the following to the IP address of your ResourceManager node, or qualified node name. Below IP address is an example.
```>>>RM_DOMAIN = '127.0.0.1'```

Set Resource Manager port variable to the actual port used:
```>>>RM_PORT = '8088'```

Let's find Cluster Name, Cluster Version, Stack and Stack Version:
```>>>restAPI='/api/v1/clusters'```
```>>>url="http://"+AMBARI_DOMAIN+":"+AMBARI_PORT+restAPI```
```>>>r=requests.get(url, auth=(AMBARI_USER_ID, AMBARI_USER_PW))```
```>>>json_data=json.loads(r.text)```
```>>>CLUSTER_NAME = json_data["items"][0]["Clusters"]["cluster_name"]```
```>>>print(CLUSTER_NAME)```
```>>>CLUSTER_VERSION =json_data["items"][0]["Clusters"]["version"]```
```>>>print(CLUSTER_VERSION)```
```>>>STACK = CLUSTER_VERSION.split('-')[0]```
```>>>print(STACK)```
```>>>STACK_VERSION = CLUSTER_VERSION.split('-')[1]```
```>>>print(STACK_VERSION)```
```>>>CLUSTER_INFO=json_data```
```>>>print(CLUSTER_INFO)```

Let's find stack repository:
```>>>restAPI = "/api/v1/stacks/"+STACK+"/versions/"+STACK_VERSION+"/operating_systems/redhat7/repositories/"+CLUSTER_VERSION```
```>>>url = "http://"+AMBARI_DOMAIN+":"+AMBARI_PORT+restAPI```
```>>>r= requests.get(url, auth=(AMBARI_USER_ID, AMBARI_USER_PW))```
```>>>json_data=json.loads(r.text)```
```>>>print(json_data)```
```>>> REPOSITORY_NAME=json_data["Repositories"]["latest_base_url"]```
```>>> print(REPOSITORY_NAME)```

A more elegant approach is to create utility functions. See restAPIFunctions.py script.
