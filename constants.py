#-------------
# Description
#-------------
# File contains all variable constants needed for calculations

# import packages
import numpy as np
class constants:
    def mu_constants(roadSurf):
        mu = np.zeros((1), dtype='d')
        for x in range(0, len(roadSurf)):
            #------------------------------------------------------
            # Road surface friction coefficients with rubber wheel
            #------------------------------------------------------

            # Concrete
            #------------------------------------------------------
            if roadSurf[x] == 1:
                mu_CDryStat = 0.65 # concrete dry static
                mu_CDryDyn  = 0.5  # concrete dry dynamic
                mu[0] = 0.65; mu = np.append(mu,0.5)
            elif roadSurf[x] == 2:
                mu_CWetStat = 0.4  # concrete wet static
                mu_CWetDyn  = 0.35 # concrete wet dynamic
                if mu[0] == 0: mu[0] = mu_CWetStat; mu = np.append(mu,mu_CWetDyn)
                else: mu = np.append(mu,mu_CWetStat); mu = np.append(mu,mu_CWetDyn)
            
            # Ice
            #------------------------------------------------------
            elif roadSurf[x] == 3:
                mu_IDryStat = 0.2  # Ice dry static
                mu_IDryDyn  = 0.15 # Ice dry static
                if mu[0] == 0: mu[0] = 0.2; mu = np.append(mu,0.15)
                else: mu = np.append(mu,0.2); mu = np.append(mu,0.15)
            elif roadSurf[x] == 4:
                mu_IWetStat = 0.1  # Ice wet dynamic
                mu_IWetDyn  = 0.08 # Ice wet dynamic
                if mu[0] == 0: mu[0] = mu_IWetStat; mu = np.append(mu,mu_IWetDyn)
                else: mu = np.append(mu,mu_IWetStat); mu = np.append(mu,mu_IWetDyn)

            # Water
            #------------------------------------------------------
            elif roadSurf[x] == 5:
                mu_WDAquPlanStat = 0.1  # water aquaplaning static
                mu_WDAquPlanDyn  = 0.05 # water aquaplaning dynamic
                if mu[0] == 0: mu[0] = mu_WDAquPlanStat; mu = np.append(mu,mu_WDAquPlanDyn)
                else: mu = np.append(mu,mu_WDAquPlanStat); mu = np.append(mu,mu_WDAquPlanDyn)

            # Gravel
            #------------------------------------------------------
            elif roadSurf[x] == 6:
                mu_GDryDyn = 0.35 # Gravel dry dynamic
                if mu[0] == 0: mu[0] = mu_GDryDyn
                else: mu = np.append(mu,mu_GDryDyn)

            # Sand
            #------------------------------------------------------
            elif roadSurf[x] == 7:
                mu_SDryDyn = 0.3 # Sand dry dynamic
                if mu[0] == 0: mu[0] = mu_SDryDyn
                else: mu = np.append(mu,mu_SDryDyn)
        return mu