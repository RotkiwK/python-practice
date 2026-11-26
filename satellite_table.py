import math 


MU = 398600.4418 # km^3/s^2
EARTH_RADIUS = 6378.137 # in km
MINUTES_PER_DAY = 1440

def altitude_from_mean_motion(mean_motion):
    mean_motion_rad = (mean_motion * 2 * math.pi) / 86400
    orbital_radius = (MU / (mean_motion_rad ** 2)) ** (1/3)
    altitude = orbital_radius - EARTH_RADIUS
    return altitude


def period_from_mean_motion(mean_motion):
    period = MINUTES_PER_DAY / mean_motion
    return period


print(round (period_from_mean_motion(15.5),1))


