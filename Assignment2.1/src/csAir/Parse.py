#!/usr/local/bin/python2.7
# encoding: utf-8
'''
csAir.Parse -- shortdesc

csAir.Parse is a class that parses the json file and creates the graph

It defines classes_and_methods

@author:     miguel

@copyright:  2014 organization_name. All rights reserved.

@license:    license

'''
from City import City
from Route import Route
import Menu
import json

'''
PARSING & CREATING THE GRAPH
'''
#First JSON
jsonData=open('csAirData')
json_csAirData = json.load(jsonData)
metros = json_csAirData["metros"]
routes = json_csAirData["routes"]
jsonData.close()
cityList=[]
routeList=[]

#Second JSON
jsonData=open('champaignData')
json_Champaign = json.load(jsonData)
metrosChamp = json_Champaign["metros"]
routesChamp = json_Champaign["routes"]
jsonData.close()

#Graph function
def createGraph(cities,routes):
    for item in cities :
        code = item.get("code")
        name = item.get("name")
        country = item.get("country")
        continent = item.get("continent")
        timezone = item.get("timezone")
        coordinates = item.get("coordinates")
        population = item.get("population")
        region = item.get("region")
        newCity= City(code, name, country, continent, timezone, coordinates, population, region)       
        cityList.append(newCity)
    for itemRoutes in routes:
        ports=itemRoutes.get("ports") 
        newRoute= Route(ports[0],ports[1],itemRoutes.get("distance"))
        routeList.append(newRoute) 
        
#Creating the Graph (Adding City to a city array)  
createGraph(metros,routes)
createGraph(metrosChamp,routesChamp)    

'''
MENU TEXT BASED USER INTERFACE
'''
Menu.startMenu(cityList, routeList)     