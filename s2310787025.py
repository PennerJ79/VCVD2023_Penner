#-------------
# Description
#-------------
# Simulation takes input from user on vehicle mass, an initial vehicle speed,
# and a selected road type. It then uses this information to simulate how long
# it will take for the vehicle to come to a standstill along with the traveled
# distance. Losses taken into consideration are: rolling resistance, and 
# aerodynamic resistance.

#-------------
# User inputs
#-------------
# - Vehicle mass
# - Initial vehicle velocity
# - Road surface type
# - Road inclination

#--------------------
# Simulation outputs
#--------------------
# A plot of vehicle velocity over time is created along with a plot of distance
# over time.

#-----------------
# import packages
#-----------------
import numpy as np
import argparse
from scipy.constants import g as gravity
import matplotlib.pyplot as plt
import create_parameters as cp
import constants as cnst
import calculation_methods as cm

def main ():   
    # --------------------------------------------------
    # initialize time variables
    # --------------------------------------------------
    time = 0 # start time
    time_step = 0.01 # s (time step)
    timeArray = np.array(0) # initialize time array

    # -----------------------------------------------------
    # use argparser to select specific friction coefficient
    # -----------------------------------------------------
    parser = argparse.ArgumentParser(description='Choose specific friction coefficient value')
    parser.add_argument('-f','--friction', type=float, default=1, \
                        help='Specify alternative surface friction coefficient')
    args = parser.parse_args()
    mu = args.friction

    # --------------------------------------------------
    # initialize and retrieve simulation parameters + constants
    # --------------------------------------------------
    print('\nPlease enter desired simulation parameters')
    if mu == 1:
        roadSurf, RS_names = cp.parameters.usrRoadSurface()
    else:
        RS_names = {'1': 'User defined mu'}
        roadSurf = np.array([1])
    vehMass = cp.parameters.vehMass() # kg
    slopeAng, percGrade = cp.parameters.slopeAng() # %
    vel0 = cp.parameters.initialVelocity() # m/s

    vStat = 1 # [m/s] speed where dynamic coefficient of friction changes to static value if available
    velocity = vel0 # m/s
    velocityPrev = velocity # m/s
    dist = 0 # distance parameter for t0
    distPrev = dist # distance of previous time step
    velArray = np.array((vel0 * 3.6)) # velocity array
    distArray = np.array(0) # distance array
    distArraySave = {}
    timeArraySave = {}
    velArraySave = {}

    #-------------------------------------------------------------
    # retrieve coefficients of friction for desired road surfaces
    # Input parameters: array of road surface numbers
    #-------------------------------------------------------------
    if mu == 1:
        mu_array = cnst.constants.mu_constants(roadSurf)
    else:
        mu_array = np.array([1])
    mu_cnt = 0
    for i in range(len(roadSurf)):
        if mu != 1:
            muDyn = mu
            muStat = mu
        else:
            if roadSurf[i] >= 1 and roadSurf[i] < 6: # for road surfaces with static and dynamic mu
                # set static and dynamic mu from save mu_array
                mu_cnt += 2
                muDyn = mu_array[mu_cnt-1]
                muStat = mu_array[mu_cnt-2]
            else: # for road surfaces only dynamic mu
                # set dynamic mu from save mu_array
                mu_cnt += 1
                muDyn = mu_array[mu_cnt-1]
                muStat = muDyn

        while velocity > 0:
            if velocity > vStat and time == 0:
                FtotLoss = cm.calculations.forces_calc(vehMass, gravity, velocity, muStat, muDyn, slopeAng, vStat) # N
                ForcesFlag = True
            elif velocity < vStat and ForcesFlag == True:
                FtotLoss = cm.calculations.forces_calc(vehMass, gravity, velocity, muStat, muDyn, slopeAng, vStat) # N
                ForcesFlag = False
                
            # acceleration calculated only once since no dynamically changing forces during simulation
            if time == 0:
                acc = cm.calculations.acc_calc(FtotLoss, vehMass)

            # dist = cm.calculations.distance_calc(dist, velocity, acc, time, time_step) # m
            dist = cm.calculations.distance_calc(velocity, time_step, acc, dist, vStat)
            distArray = np.append(distArray, dist)

            # velocity = cm.calculations.velocity_calc(Wkin, vehMass)
            velocity = cm.calculations.velocity_calc(velocity, acc, time_step)
            velArray = np.append(velArray, (velocity * 3.6))
            time += time_step
            timeArray = np.append(timeArray, time)
        
        # save simulation run values to dictionaries
        distArraySave[i] = distArray
        velArraySave[i] = velArray
        timeArraySave[i] = timeArray

        # reset simulation variables to zero
        velocity = vel0; velocityPrev = vel0 # reset velocity variables
        time = 0 # reset time
        dist = 0 # reset traveled distance
        distArray = np.array(0) # reset distance array
        velArray = np.array(vel0 * 3.6) # reset velocity array
        timeArray = np.array(0) # reset time array

    #-------------------------
    # plot simulation results
    #-------------------------
    # create plot for velocity over time
    fig1 = plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)        
    for i in range(len(velArraySave)):
        timePlot = np.array(timeArraySave[i])
        timePlot = timePlot[0:len(velArraySave[i])]
        lineName = RS_names[str(roadSurf[i])]
        plt.plot(timePlot, velArraySave[i], linewidth=1, label=lineName)
        plt.title('Vehicle velocity over time')
        plt.ylabel('Velocity [km/h]')
        plt.xlabel('Time [s]')
        plt.legend()

    # create plot for distance over time
    plt.subplot(1,2,2) 
    for i in range(len(distArraySave)):
        timePlot = np.array(timeArraySave[i])
        timePlot = timePlot[0:len(distArraySave[i])]
        lineName = RS_names[str(roadSurf[i])]
        plt.plot(timePlot, distArraySave[i], linewidth=1, label=lineName)
        plt.title('Vehicle distance over time')
        plt.ylabel('Distance [m]')
        plt.xlabel('Time [s]')
        plt.legend()

    simInfo = ('Simulation parameters: dynamic mu = ') + str(round(muDyn,2)) + (', mass = ') + str(vehMass) \
        + ('kg, grade = ') + str(percGrade) + ('%, velocity = ') + str(vel0*3.6) + ('km/h')
    print(simInfo)
    plt.suptitle(simInfo)
    plt.show()

if __name__ == '__main__':
    main()