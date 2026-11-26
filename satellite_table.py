import math 


MU = 398600.4418 
EARTH_RADIUS = 6378.137 # in km

def altitude_from_mean_motion(mean_motion):
    mean_motion_rad = (mean_motion * 2 * math.pi) / 86400
    orbital_radius = (MU / (mean_motion_rad ** 2)) ** (1/3)
    altitude = orbital_radius - EARTH_RADIUS
    return altitude

altitude_rounded = round (altitude_from_mean_motion(15.5), 1)
print(altitude_rounded)