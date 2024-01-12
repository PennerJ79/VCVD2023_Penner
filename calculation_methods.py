#-------------
# Description
#-------------
# Contains calculations methods for simulation

# import packages
import math
from scipy.constants import g as gravity

class calculations:
    #-----------------------------------------------------------------------------------------
    # Force calculations: determine force due to friction and slope angle, then sum into total
    # Input parameters: mass(kg), gravity(m/s^2), velocity(m/s), dynamic friction coefficient,
    #                   static friction coefficient, slope angle
    #-----------------------------------------------------------------------------------------
    def forces_calc(vehMass, gravity, velocity, muStat, muDyn, slopeAng, vStat):
        # Normal force
        FN = vehMass * gravity # N

        # Frictional force (total for 4 tires)
        if velocity < vStat: # (km/h)
            FR = muStat * FN * math.cos(slopeAng) # N
        else:
            FR = muDyn * FN * math.cos(slopeAng) # N

        # Slope force
        Fslope = FN * math.sin(slopeAng) # N
        return (-FR) + (-Fslope) # N
    
    ###----------------------------------------------------------------------
    # Calculation of change in distance
    # Input parameters: previous distance, velocity, time step, acceleration
    ###----------------------------------------------------------------------
    def distance_calc(velocity, time_step, acc, dist, vStat):
        if velocity < vStat: # (km/h)
            # dist = (velocity - velocityPrev)**2 / (2 * gravity * muStat * (math.cos(slopeAng) + math.sin(slopeAng)))
            dist = dist + (velocity * time_step) + (0.5 * acc * time_step**2)
        else:
            # dist = (velocity - velocityPrev)**2 / (2 * gravity * muDyn * (math.cos(slopeAng) + math.sin(slopeAng)))
            dist = dist + (velocity * time_step) + (0.5 * acc * time_step**2)
        return dist # m

    ##------------------------------------------------------------------------------
    # Calculation of vehicle velocity
    # Input parameters: curr. sim. time, last vehicle velocity, current acceleration
    ##------------------------------------------------------------------------------
    def velocity_calc(velocity, acc, time_step):
        velocity  = velocity + (acc * time_step)
        return velocity # m/s
    
    ###-----------------------------------------------------------------
    # Calculation of vehicle acceleration
    # Input parameters: velocity, current time, previous time step time
    ###-----------------------------------------------------------------
    def acc_calc(FtotLoss, vehMass):
        acc = FtotLoss / vehMass
        return acc # m/s^2
    
    ###-----------------------------------------------------
    # Calculation of energy losses
    # Input parameters: total forces from environment losses
    ###-----------------------------------------------------
    def W_loss_calc(FtotLoss, time_step):
        return FtotLoss * time_step # J

    #------------------------------------------
    # Calculation of vehicle work
    # Input parameters: mass, current velocity
    #------------------------------------------
    def Wkin_calc(vehMass, velocity, W_loss):
        return ((vehMass * velocity**2) / 2) + W_loss # [J] negative W_loss
    
    #------------------------------------------
    # Calculations for rule of thumb
    # Input parameters: 
    #------------------------------------------
    def ruleThumb(vel0, distArray, i, RS_names, roadSurf):
        distNormal = (vel0 / 10)**2 # normal distance
        distDanger = ((vel0 / 10)**2) * 0.5 # distance danger
        distReaction = ((vel0 / 10)**2) * 3 # distance reaction
        distStop = distNormal + distReaction # distance stopping
        distDanger = distDanger + distReaction # distance stopping dangerous
        print('\n\nRule of thumb stopping distances based on vehicle speed'
                '\n-------------------------------------------------------\n')
        print('Normal stopping distance: %0.2f' % (distStop) + 'm')
        print('Danger stopping distance: %0.2f' % (distDanger) + 'm')
        print('\nSimulated stopping distance only from coasting with road/tire friction losses')
        print('Simulated traveled distance for ' + RS_names[str(roadSurf[i])] \
              + ': %0.02f' % (distArray[-1]) + '\n\n')