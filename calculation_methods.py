#-------------
# Description
#-------------
# Contains calculations methods for simulation

"""import packages"""
import math
from scipy.constants import g as gravity

# class calculations:
#-----------------------------------------------------------------------------------------
# Force calculations: determine force due to friction and slope angle, then sum into total
# Input parameters: mass(kg), gravity(m/s^2), velocity(m/s), dynamic friction coefficient,
#                   static friction coefficient, slope angle
#-----------------------------------------------------------------------------------------
def forces_calc(veh_mass, velocity, mu_stat, mu_dyn, slope_ang, v_stat):
    """Calculate generated forces"""
    # Normal force
    fn = veh_mass * gravity # N

    # frictional force (total for 4 tires)
    if velocity < v_stat: # (km/h)
        fr = mu_stat * fn * math.cos(slope_ang) # N
    else:
        fr = mu_dyn * fn * math.cos(slope_ang) # N

    # Slope force
    f_slope = fn * math.sin(slope_ang) # N
    return (-fr) + (-f_slope) # N

###----------------------------------------------------------------------
# Calculation of change in distance
# Input parameters: previous distance, velocity, time step, acceleration
###----------------------------------------------------------------------
def distance_calc(velocity, time_step, acc, dist, v_stat):
    """find change in distance per time step"""
    if velocity < v_stat: # (km/h)
        dist = dist + (velocity * time_step) + (0.5 * acc * time_step**2)
    else:
        dist = dist + (velocity * time_step) + (0.5 * acc * time_step**2)
    return dist # m

##------------------------------------------------------------------------------
# Calculation of vehicle velocity
# Input parameters: curr. sim. time, last vehicle velocity, current acceleration
##------------------------------------------------------------------------------
def velocity_calc(velocity, acc, time_step):
    """find change in velocity per time step"""
    velocity  = velocity + (acc * time_step)
    return velocity # m/s

###-----------------------------------------------------------------
# Calculation of vehicle acceleration
# Input parameters: velocity, current time, previous time step time
###-----------------------------------------------------------------
def acc_calc(f_tot_loss, veh_mass):
    """calculate the acceleration"""
    acc = f_tot_loss / veh_mass
    return acc # m/s^2
