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

"""import packages"""
import argparse
import numpy as np
import matplotlib.pyplot as plt
import create_parameters as cp
import constants as cnst
import calculation_methods as cm

def main ():
    """main simulation code"""
    # --------------------------------------------------
    # initialize time variables
    # --------------------------------------------------
    time = 0 # start time
    time_step = 0.01 # s (time step)
    time_array = np.array(0) # initialize time array

    # -------------------------------------------------------------
    # creation of argparser to select specific friction coefficient
    # -------------------------------------------------------------
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
        road_surf, rs_names = cp.usrroad_surface()
    else:
        rs_names = {'1': 'User defined mu'}
        road_surf = np.array([1])
    veh_mass = cp.vehicle_mass() # kg
    slope_ang, perc_grade = cp.slope_angle() # %
    vel0 = cp.initial_velocity() # m/s

    v_stat = 1 # [m/s] speed where dynamic mu changes to static value if available
    velocity = vel0 # m/s
    dist = 0 # distance parameter for t0
    vel_array = np.array((vel0 * 3.6)) # velocity array
    dist_array = np.array(0) # distance array
    dist_array_save = {}
    time_array_save = {}
    vel_array_save = {}

    #-------------------------------------------------------------
    # retrieve coefficients of friction for desired road surfaces
    # Input parameters: array of road surface numbers
    #-------------------------------------------------------------
    if mu == 1:
        mu_array = cnst.mu_constants(road_surf)
    else:
        mu_array = np.array([1])
    mu_cnt = 0
    for i in range(len(road_surf)):
        if mu != 1:
            mu_dyn = mu
            mu_stat = mu
        else:
            if road_surf[i] >= 1 and road_surf[i] < 6: # for surfaces with static and dynamic mu
                # set static and dynamic mu from save mu_array
                mu_cnt += 2
                mu_dyn = mu_array[mu_cnt-1]
                mu_stat = mu_array[mu_cnt-2]
            else: # for road surfaces only dynamic mu
                # set dynamic mu from save mu_array
                mu_cnt += 1
                mu_dyn = mu_array[mu_cnt-1]
                mu_stat = mu_dyn

        while velocity > 0:
            if velocity > v_stat and time == 0:
                f_tot_loss = cm.forces_calc(veh_mass, velocity, \
                                                         mu_stat, mu_dyn, slope_ang, v_stat) # N
                forces_flag = True
            elif velocity < v_stat and forces_flag:
                f_tot_loss = cm.forces_calc(veh_mass, velocity, \
                                                         mu_stat, mu_dyn, slope_ang, v_stat) # N
                forces_flag = False

            # acceleration calculated only once since no dynamically
            # changing forces during simulation
            if time == 0:
                acc = cm.acc_calc(f_tot_loss, veh_mass)

            # dist = cm.distance_calc(dist, velocity, acc, time, time_step) # m
            dist = cm.distance_calc(velocity, time_step, acc, dist, v_stat)
            dist_array = np.append(dist_array, dist)

            # velocity = cm.velocity_calc(Wkin, veh_mass)
            velocity = cm.velocity_calc(velocity, acc, time_step)
            vel_array = np.append(vel_array, (velocity * 3.6))
            time += time_step
            time_array = np.append(time_array, time)

        # save simulation run values to dictionaries
        dist_array_save[i] = dist_array
        vel_array_save[i] = vel_array
        time_array_save[i] = time_array

        # reset simulation variables to zero
        velocity = vel0 # reset velocity variables
        time = 0 # reset time
        dist = 0 # reset traveled distance
        dist_array = np.array(0) # reset distance array
        vel_array = np.array(vel0 * 3.6) # reset velocity array
        time_array = np.array(0) # reset time array

    #-------------------------
    # plot simulation results
    #-------------------------
    # create plot for velocity over time
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    for i in range(len(vel_array_save)):
        time_plot = np.array(time_array_save[i])
        time_plot = time_plot[0:len(vel_array_save[i])]
        line_name = rs_names[str(road_surf[i])]
        plt.plot(time_plot, vel_array_save[i], linewidth=1, label=line_name)
        plt.title('Vehicle velocity over time')
        plt.ylabel('Velocity [km/h]')
        plt.xlabel('Time [s]')
        plt.legend()

    # create plot for distance over time
    plt.subplot(1,2,2)
    for i in range(len(dist_array_save)):
        time_plot = np.array(time_array_save[i])
        time_plot = time_plot[0:len(dist_array_save[i])]
        line_name = rs_names[str(road_surf[i])]
        plt.plot(time_plot, dist_array_save[i], linewidth=1, label=line_name)
        plt.title('Vehicle distance over time')
        plt.ylabel('Distance [m]')
        plt.xlabel('Time [s]')
        plt.legend()

    sim_info = ('Simulation parameters: dynamic mu = ') + str(round(mu_dyn,2)) \
        + (', mass = ') + str(veh_mass) + ('kg, grade = ') + str(perc_grade) \
        + ('%, velocity = ') + str(vel0*3.6) + ('km/h')
    print(sim_info)
    plt.suptitle(sim_info)
    plt.show()

if __name__ == '__main__':
    main()
