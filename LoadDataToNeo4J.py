# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 17:07:21 2017

@author: Amaresh
"""

from neo4j.v1 import GraphDatabase, basic_auth

driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "hadoop"))
session = driver.session()


def doesNodeExist(nodeName):
    #result = session.run("MATCH (a:Person) WHERE a.name ={name} "
    #                   "RETURN count(*)",
    #                  {"name": nodeName})
    result = session.run("MATCH (a:Device) WHERE a.name = {name} "
                       "RETURN a.name AS name",
                       {"name": nodeName})  
    count=0
    for record in result:
        print("%s" % (record["name"]))
        count= count+1
    if count > 0:
        return True
    else:
        return False



def createNode(nodeName):   
    session.run("CREATE (a:Device {name: {name}})",{"name": nodeName})
  

def createMultipleNode():
    with open("test.txt","r") as f:
        for nodeName in f:
            if not doesNodeExist(nodeName):
                createNode(nodeName)
    f.close()
    
    
def createRelation():
        
    
createMultipleNode()
session.close()

