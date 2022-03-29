#====================================================================================================================================
import requests #For APIs
import time #For timing how long all this stuff takes
import sys #for extra functions, such as exit
#If you get errors on the above imports, run the following from an elevated command prompt: 
# py -m pip install requests
#====================================================================================================================================
#=============================================Created by CMDR Longman.P.J.===========================================================
#====================================================================================================================================

def HGEhunter() :
    print("HGE Hunter - By: Pete#1168")
    
    print("Downloading EDDB Stations & Populated Systems")
    startTime = time.time()
    #rawEddbStations = requests.get( "https://eddb.io/archive/v6/stations.json" ).json()
    rawEddbPopulatedSystems = requests.get( "https://eddb.io/archive/v6/systems_populated.json" ).json()
    print(f"Download Took {round(time.time() - startTime, 2)} Seconds")
    print("1: Core Dynamics Composites")
    print("2: Imperial Shielding")
    print("3: Improvised Components")
    print("4: Military Grade Alloys/Supercapacitors")
    print("5: Pharmaceutical Isolators")
    print("6: Proto Heat Radiators/Radiolic Alloys")
    counter = 0
    counter2 = 0
    while counter < 4:
        try:
            HGEnum_input = int(input("Enter a number for the HGE you are hunting: "))
            counter = counter + 1
            if  1 <= HGEnum_input <= 6:
                break
        except ValueError:
            print("This is not a valid input. Try again.")
            counter2 = counter2 +1
            if counter2 >= 4:
                print("You entered too many erroneous inputs. This program will exit.")
                sys.exit(0)
    if counter >= 4:
            print("You entered too many erroneous inputs. This program will exit.")
            sys.exit(0)        
    print(f"You entered {HGEnum_input}")  
    print(f"Filtering {len(rawEddbPopulatedSystems)} Systems By State & Allegiance")
    startTime = time.time()
    outputSystems = [] #system details, system population
    for rawEddbPopulatedSystem in rawEddbPopulatedSystems :
        allegiance = rawEddbPopulatedSystem["allegiance"] #allegiance=="Empire" "Federation" or "Independent"
        emp = False #Empire
        fed = False #Federation
        ind = False #Independent

        if allegiance=="Empire" :
            emp = True
        elif allegiance=="Federation" :
            fed = True
        elif allegiance=="Independent" :
            ind = True          
        states = rawEddbPopulatedSystem["states"] 
        #cleanStates = []
        bom = False #Boom
        war = False #War
        out = False #Outbreak
        unr = False #Civil Unrest
        hss = True #if any of the above are in the sys state, this is False (hss = HGE special state)
        sct = 0 #Counts number of special states are active simultaneously
        for stateGroup in states :
            state = stateGroup["name"] #Just grab the name of the state
            #if state != "None" :
            #    cleanStates.append( state )
            if (state=="Boom") :
                bom = True
                hss = False
                sct = sct + 1
            elif (state=="Civil Unrest") :
                unr = True
                hss = False
                sct = sct + 1
            elif (state=="Outbreak") :
                out = True
                hss = False
                sct = sct + 1
            elif (state=="War" or state=="Civil War") :
                war = True
                hss = False
                sct = sct + 1
        countsys = 0
        match HGEnum_input:
            case 1:
                if emp and hss :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 10000000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
            case 2:
                if fed and hss :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 10000000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
            case 3:
                if unr and ind and (not hss) :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 1000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
            case 4:
                if war and ind and sct == 1 :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 1000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
            case 5:                          
                if out and ind and sct == 1 :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 1000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
            case 6:
                if bom and ind and sct == 1 :
                    pop = int(rawEddbPopulatedSystem["population"])
                    if pop >= 5000000000 :
                        sysName = rawEddbPopulatedSystem["name"]
                        outputSystems.append([int(pop), sysName])
    print(f"Filtering Took {round(time.time() - startTime, 2)} Seconds")
    print(f"Printing Final Results\n")
    outputSystems.sort(reverse=True)
    outputSystems.reverse()
    import re
    for index in outputSystems :
        index2 = str(index)
        res = index2.find(",")
        res2 = (res + 3)
        res3 = len(index2)
        res4 = (res2 - res - 5)
        pop = format(int(index2[1:res]), ",")
        match res :
            case 12:
                popspc = "Population: " 
            case 11:
                popspc = "Population:  "
            case 10:
                popspc = "Population:    "
            case 9:
                popspc = "Population:     "
            case 8:
                popspc = "Population:      "        
        sysnm = str(index2[res2:res4])
        index3 = popspc + pop + " System: " +sysnm
        #print(res)
        #print(res2)
        #print(res3)
        #print(index2)
        print(index3) 
    print() #newline
    input("Press the Enter key to exit - ")
#====================================================================================================================================

if __name__ == "__main__":
    HGEhunter()

#====================================================================================================================================
