'''
Created on Mar 5, 2014

@author: miguel
'''
from City import City
from Route import Route

line="-" * 105 
#Function to edit the route network
def editing(cityList,routeList):
        
        #Functions used afterwards        
        def find_city(cityList, name):
            for city in cityList:
                if city.name == name:
                    return city
            
        def find_route(routeList, origin_, dest_):
            for route in routeList:
                if route.origin==origin_ and route.dest == dest_:
                    return route
                
        def find_routeDelete(code):
            for route in routeList:
                if route.origin==code or route.dest == code:
                    routeList.remove(route)          
                     
        def addCity():
            code = int(input("Enter code:"))
            name = input("name:")
            country =input("country:")
            continent = input("continent:")
            timezone = int(input("timezone:"))
            coordinates = int(input("coordinates:"))
            population = int(input("population:"))
            region = int(input("region:"))
            newCity=City(code, name, country, continent, timezone, coordinates, population, region)
            return newCity
        
        def addRoute():
            origin = int(input("Enter origin:"))
            dest = input("Enter destination:")
            distance =input("Enter distance:")
            newRoute=Route(origin, dest, distance)
            return newRoute
                                     
        print('+'+line+'+')
        print("1.Remove city")
        print("2.Remove route")
        print("3.Add city")
        print("4.Add route")
        print("5.Edit existing city")
        print('+'+line+'+')
        
        editingOpt = int(input("Input your option: "))

        def removeC():
            rCity = input("Which city do you want to remove: ")
            cityPick=find_city(cityList, rCity)
            cityList.remove(cityPick)
            
            #Remove also all its routes
            find_routeDelete(cityPick.code)
        
        def removeR():
            print("Which route do you want to delete")
            origin = input("Which origin: ")
            dest = input("Which destination: ")
            routePick=find_route(routeList, origin, dest)
            routeList.remove(routePick)
 
        def addC():
            print("Which city do you want to add")
            newCity= addCity() 
            cityList.append(newCity)
        
        def addR():
            print("Which route do you want to add")
            newRoute= addRoute() 
            routeList.append(newRoute)
        
        #Since in the assignment it doesn't say what can we edit
        def edit():
            eCityName = input("Name of the city you want to edit:")
            cityPick=find_city(cityList, eCityName)
            edit = input("What do you want to edit")
            print("code")
            print("name")
            if(edit=="name"):
                name = input("New name: ")
                cityPick.name=name
            if(edit=="code"):
                code = input("New code: ")
                cityPick.code=code  
        
        optMenuStaticDicc = {
                        1 : removeC,
                        2 : removeR,
                        3 : addC,
                        4 : addR,
                        5 : edit,
        }
        optMenuStaticDicc[editingOpt]()