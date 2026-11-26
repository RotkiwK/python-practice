import math 
import pandas as pd 


MU = 398600.4418 # km^3/s^2
EARTH_RADIUS_KM = 6378.137 # in km
MINUTES_PER_DAY = 1440


def altitude_from_mean_motion(mean_motion):
    mean_motion_rad = (mean_motion * 2 * math.pi) / 86400
    orbital_radius = (MU / (mean_motion_rad ** 2)) ** (1/3)
    altitude = orbital_radius - EARTH_RADIUS_KM
    return altitude


def period_from_mean_motion(mean_motion):
    period = MINUTES_PER_DAY / mean_motion
    return period


satellites = [
    {"NAME": "ISS", "MEAN_MOTION": 15.50},
    {"NAME": "Hubble", "MEAN_MOTION": 15.09},
    {"NAME": "Tiangong", "MEAN_MOTION": 15.60},
    {"NAME": "NOAA-20", "MEAN_MOTION": 14.19},
    {"NAME": "GPS", "MEAN_MOTION": 2.0056}
]


df = pd.DataFrame(satellites)
df["ALTITUDE_KM"] = altitude_from_mean_motion(df["MEAN_MOTION"])
df["PERIOD_MIN"] = period_from_mean_motion(df["MEAN_MOTION"])
print(df)