#-------------
# Description
#-------------
# File asks for user input for required input parameters

"""import packages"""
import math
import numpy as np

#------------------------------
# user defined road surface(s)
#------------------------------
def usrroad_surface():
    """retrieve desired road surface from user"""
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
    road_surf = np.zeros((num), dtype=int)

    for i in range(num):
        input_flag = True
        while input_flag:
            usr_in = int(input("\nRoad surface %0.0f of %0.0f: " %((i+int(1)), num)))
            if usr_in < 1 or usr_in > 7:
                print("\nInvalid input, please enter a valid selection")
            else: input_flag = False
        road_surf[i] = usr_in
    road_surf = np.sort(road_surf)

    print("\nSelected road surfaces:")
    for x in range(0, len(road_surf)):
        if road_surf[x] == 1:
            print("concrete dry dynamic")
        elif road_surf[x] == 2:
            print("concrete wet dynamic")
        elif road_surf[x] == 3:
            print("Ice dry dynamic")
        elif road_surf[x] == 4:
            print("Ice wet dynamic")
        elif road_surf[x] == 5:
            print("water aquaplaning dynamic")
        elif road_surf[x] == 6:
            print("Gravel dry dynamic")
        elif road_surf[x] == 7:
            print("Sand dry dynamic")
        else:
            print("No valid entry selected")

    # create dictionary for road surface names
    rs_names = {'1': 'concrete dry dynamic', '2': 'concrete wet dynamic', '3': 'Ice dry dynamic',
                '4': 'Ice wet dynamic', '5': 'water aquaplaning dynamic', '6': 'Gravel dry dynamic',
                '7': 'Sand dry dynamic',}
    return road_surf, rs_names

#---------------------------
# user defined vehicle mass
#---------------------------
def vehicle_mass():
    """return vehicle mass"""
    veh_mass = int(input("\nVehicle mass [kg]: "))
    return veh_mass

#--------------------------
# user defined slope angle
#--------------------------
def slope_angle():
    """return road slope angle"""
    perc_grade = int(input("\nRoad grade [%]: "))
    slope_ang = math.atan(perc_grade/100) # conversion of slope percentage to radians
    return slope_ang, perc_grade # degrees

#---------------------------------------
# user defined initial vehicle velocity
#---------------------------------------
def initial_velocity():
    """return vehicles initial velocity"""
    vel0 = int(input("\nInitial vehicle velocity [km/h]: ")) # km/h
    vel0 = vel0 / 3.6 # convert given velocity from km/h to m/s
    return vel0 # m/s
