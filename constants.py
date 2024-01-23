#-------------
# Description
#-------------
# File contains all variable constants needed for calculations

"""import packages"""
import numpy as np

def mu_constants(road_surf):
    """mu constant look-up table"""
    mu = np.zeros((1), dtype='d')
    for x in range(0, len(road_surf)):
        #------------------------------------------------------
        # Road surface friction coefficients with rubber wheel
        #------------------------------------------------------

        # Concrete
        #------------------------------------------------------
        if road_surf[x] == 1:
            mu_cdry_stat = 0.65 # concrete dry static
            mu_cdry_dyn  = 0.5  # concrete dry dynamic
            mu[0] = mu_cdry_stat
            mu = np.append(mu,mu_cdry_dyn)
        elif road_surf[x] == 2:
            mu_cwet_stat = 0.4  # concrete wet static
            mu_cwet_dyn  = 0.35 # concrete wet dynamic
            if mu[0] == 0:
                mu[0] = mu_cwet_stat
                mu = np.append(mu,mu_cwet_dyn)
            else:
                mu = np.append(mu,mu_cwet_stat)
                mu = np.append(mu,mu_cwet_dyn)

        # Ice
        #------------------------------------------------------
        elif road_surf[x] == 3:
            mu_idry_stat = 0.2  # Ice dry static
            mu_idry_dyn  = 0.15 # Ice dry static
            if mu[0] == 0:
                mu[0] = mu_idry_stat
                mu = np.append(mu,mu_idry_dyn)
            else:
                mu = np.append(mu,0.2)
                mu = np.append(mu,0.15)
        elif road_surf[x] == 4:
            mu_iwet_stat = 0.1  # Ice wet dynamic
            mu_iwet_dyn  = 0.08 # Ice wet dynamic
            if mu[0] == 0:
                mu[0] = mu_iwet_stat
                mu = np.append(mu,mu_iwet_dyn)
            else:
                mu = np.append(mu,mu_iwet_stat)
                mu = np.append(mu,mu_iwet_dyn)

        # Water
        #------------------------------------------------------
        elif road_surf[x] == 5:
            mu_aquplan_stat = 0.1  # water aquaplaning static
            mu_aquplan_dyn  = 0.05 # water aquaplaning dynamic
            if mu[0] == 0:
                mu[0] = mu_aquplan_stat
                mu = np.append(mu,mu_aquplan_dyn)
            else:
                mu = np.append(mu,mu_aquplan_stat)
                mu = np.append(mu,mu_aquplan_dyn)

        # Gravel
        #------------------------------------------------------
        elif road_surf[x] == 6:
            mu_gdry_dyn = 0.35 # Gravel dry dynamic
            if mu[0] == 0:
                mu[0] = mu_gdry_dyn
            else:
                mu = np.append(mu,mu_gdry_dyn)

        # Sand
        #------------------------------------------------------
        elif road_surf[x] == 7:
            mu_sdry_dyn = 0.3 # Sand dry dynamic
            if mu[0] == 0:
                mu[0] = mu_sdry_dyn
            else:
                mu = np.append(mu,mu_sdry_dyn)
    return mu
