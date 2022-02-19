import numpy as np


class Dose:
    """A set of radiation doses from release"""
    def iodines_func(holdup, exposure, iodine_rate):
        

        tedi = -7036 * np.exp(holdup) * (-.4306)      -   3.426e4 * np.exp(-.009497 ) +  5.838e4 * np.exp(3.875e-4 ) * iodine_rate * exposure
        adult = 1.133e6 * np.exp(holdup) * (3.455e-4 ) -   1.504e5 * np.exp(-.2328 ) -    6.953e5 * np.exp(-.008704 ) * iodine_rate * exposure
        child = 2.047e6 * np.exp(holdup) * (4.467e-4 ) -   2.576e5 * np.exp(-.4386 ) -    1.191e6 * np.exp(-.01076 ) * iodine_rate * exposure
        .sum
        return tedi, adult, child

    def nobles(holdup, exposure, noble_rate):
        if holdup == 0:
            l_holdup = 0
        else:
            l_holdup = np.log(holdup)

        if exposure == 0:
            l_exposure = 0
        else:
            l_exposure = np.log(exposure)

        # coefficients
        
        p00 = 287.1 
        p01 = -73.16 * l_holdup 
        p02 = -17.52 * l_holdup ** 2 
        p03 = 6.866 * l_holdup ** 3 
        p04 = -0.5276 * l_holdup ** 4
        p10 = -39.3 * l_exposure 
        p11 = 22.67 * l_exposure * l_holdup 
        p12 = -4.229 * l_exposure * l_holdup ** 2 
        p13 = 0.2565* l_exposure * l_holdup ** 3
        p20 = -10.36 * l_exposure ** 2
        p21 = 4.307 * l_exposure ** 2 * l_holdup
        p22 = -0.4185 * l_exposure ** 2 * l_holdup ** 2
        p30 = -0.5556 * l_exposure ** 3 
        p31 = 0.0811 * l_exposure ** 3 * l_holdup


        tedn = noble_rate * exposure * (
            






            
        return tedn

        def __init__(self, ted: float=eff_dose, thyroid:=thy_dose):
            # Input parameters are calculated doses
            self.ted = ted
            self.tyhroid = thyroid