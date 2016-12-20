def ambariREST( restAPI ) :
    url = "http://"+AMBARI_DOMAIN+":"+AMBARI_PORT+restAPI
    r= requests.get(url, auth=(AMBARI_USER_ID, AMBARI_USER_PW))
    return(json.loads(r.text));

def rmREST( restAPI ) :
    url = "http://"+RM_DOMAIN+":"+RM_PORT+restAPI
    r=requests.get(url)
    return(json.loads(r.text));

def getClusterVersionAndName() :
    json_data = ambariREST("/api/v1/clusters")
    cname = json_data["items"][0]["Clusters"]["cluster_name"]
    cversion =json_data["items"][0]["Clusters"]["version"]
    return cname, cversion, json_data;

def getClusterRepository() :
    restAPI = "/api/v1/stacks/"+STACK+"/versions/"+STACK_VERSION+"/operating_systems/redhat7/repositories/"+CLUSTER_VERSION
    json_data = ambariREST(restAPI)
    return json_data;

def getAmbariHosts() :
    restAPI = "/api/v1/hosts"
    json_data =  ambariREST(restAPI)
    return(json_data);
    
def getConfigGroups() :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME+"/config_groups"
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getServiceConfigTypes() :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME+"/configurations"
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getServiceActualConfigurations() :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getCheckClusterForRollingUpgrades() :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME+"/rolling_upgrades_check/"
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getStackVersions() :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME+"/stack_versions/"
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getServices( SERVICE) :
    restAPI = "/api/v1/clusters/"+CLUSTER_NAME+"/services/"+SERVICE
    json_data =  ambariREST(restAPI)
    return(json_data); 

def getResourceManagerInfo() :
    restAPI = "/ws/v1/cluster/info"
    json_data =  rmREST(restAPI)
    return(json_data);

def getResourceManagerMetrics() :
    restAPI = "/ws/v1/cluster/metrics"
    json_data =  rmREST(restAPI)
    return(json_data);

def getRMschedulerInfo() :
    restAPI = "/ws/v1/cluster/scheduler"
    json_data =  rmREST(restAPI)
    return(json_data);

def getAppsSummary() :
    restAPI = "/ws/v1/cluster/apps"
    json_data =  rmREST(restAPI)
    return(json_data); 

def getAppsStatistics() :
    restAPI = "/ws/v1/cluster/appstatictics"
    json_data =  rmREST(restAPI)
    return(json_data); 
    
def getNodesSummary() :
    restAPI = "/ws/v1/cluster/nodes"
    json_data =  rmREST(restAPI)
    return(json_data); 
