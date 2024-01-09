#-------------
# Description
#-------------
# File asks for user input for required input parameters

# import packages
import numpy as np
import math

class parameters:
    #------------------------------
    # user defined road surface(s)
    #------------------------------
    def usrRoadSurface():
        print("\nAvailable road surface selections\n",
            "concrete dry      = 1\n",
            "concrete wet      = 2\n",
            "Ice dry           = 3\n",
            "Ice wet           = 4\n",
            "water aquaplaning = 5\n",
            "Gravel dry        = 6\n",
            "Sand dry          = 7\n")
        print("-------------------------------------")
        num = int(input("\nEnter number of selections you would like to make: "))
        roadSurf = np.zeros((num), dtype=int)
        
        for i in range(num):
            inputFlag = True
            while inputFlag == True:
                usrIn = int(input("\nRoad surface %0.0f of %0.0f: " %((i+int(1)), num)))
                if usrIn < 1 or usrIn > 7:
                    print("\nInvalid input, please enter a valid selection")
                else: inputFlag = False
            roadSurf[i] = (usrIn)
        roadSurf = np.sort(roadSurf)

        print("\nSelected road surfaces:")
        for x in range(0, len(roadSurf)):
            if roadSurf[x] == 1:
                print("concrete dry dynamic");
            elif roadSurf[x] == 2:
                print("concrete wet dynamic")
            elif roadSurf[x] == 3:
                print("Ice dry dynamic")
            elif roadSurf[x] == 4:
                print("Ice wet dynamic")
            elif roadSurf[x] == 5:
                print("water aquaplaning dynamic")
            elif roadSurf[x] == 6:
                print("Gravel dry dynamic")
            elif roadSurf[x] == 7:
                print("Sand dry dynamic")
            else:
                print("No valid entry selected")
            
        # create dictionary for road surface names
        RS_names = {'1': 'concrete dry dynamic', '2': 'concrete wet dynamic', '3': 'Ice dry dynamic',
                    '4': 'Ice wet dynamic', '5': 'water aquaplaning dynamic', '6': 'Gravel dry dynamic',
                    '7': 'Sand dry dynamic',}
        return roadSurf, RS_names

    #---------------------------
    # user defined vehicle mass
    #---------------------------
    def vehMass():
        vehMass = int(input("\nVehicle mass [kg]: "))
        return vehMass

    #--------------------------
    # user defined slope angle
    #--------------------------
    def slopeAng():
        percGrade = int(input("\nRoad grade [%]: "))
        slopeAng = math.atan(percGrade/100) # conversion of slope percentage to radians
        return slopeAng, percGrade # degrees

    #---------------------------------------
    # user defined initial vehicle velocity
    #---------------------------------------
    def initialVelocity():
        vel0 = int(input("\nInitial vehicle velocity [km/h]: ")) # km/h
        vel0 = vel0 / 3.6 # convert given velocity from km/h to m/s
        return vel0 # m/s