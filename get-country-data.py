import os
import pandas as pd
import numpy as np

from geopy.distance import geodesic


def get_country_data(checkin_country, df_cities, country_code):
    #### identifying cities in check-ins from countries in a very naive way
    
	checkin = checkin_country[checkin_country["CountryCode"] == country_code]
    checkin.reset_index(inplace = True, drop = True)

    cities = df_cities[df_cities["CountryCode"] == country_code]
    cities.reset_index(inplace = True, drop = True)

    name_cities = []
    for lat, long in zip(checkin.Latitude, checkin.Longitude):

        min_dist    = np.inf
        city        = ''

        for dist_city, name_city in zip(zip(cities.Latitude, cities.Longitude), cities.CityName):
            km_dist = geodesic((lat, long), dist_city).km

            if km_dist < min_dist:
                min_dist = km_dist
                city     = name_city

        name_cities.append(city)

    checkin['City'] = name_cities
    
    return checkin


################
##### LOAD DATA
###############

## POIs
path_poi = os.path.join("dataset", "dataset_TIST2015_POIs.txt")
df_poi   = pd.read_csv(path_poi, sep = "\t", header = None)

df_poi.columns = ["VenueID", "Latitude", "Longitude", "VenueName", "CountryCode"]

## Cities
path_cities = os.path.join("dataset", "dataset_TIST2015_Cities.txt")
df_cities   = pd.read_csv(path_cities, sep = "\t", header = None)

df_cities.columns = ["CityName", "Latitude", "Longitude", "CountryCode", "CountryName", "CityType"]

## Checkin
path_checkin = os.path.join("dataset", "dataset_TIST2015_Checkins.txt")
df_checkin   = pd.read_csv(path_checkin, sep = "\t", header = None)

df_checkin.columns = ["UserID", "VenueID", "Time", "Timezone"]


################
##### Join check-ins with POIs (Venue information from Foursquare)
###############

checkin_country = pd.merge(df_checkin, df_poi, how = 'left')
checkin_country.dropna(inplace = True)

## contando check-ins por países
count_checkins = checkin_country.groupby(["CountryCode"]).count()["UserID"]
print(count_checkins.sort_values(ascending = False)[:5])


################
##### Get Data by Country
###############

br_checkin = get_country_data(checkin_country, df_cities, country_code = 'BR')
br_checkin.to_csv("br_checkin.csv")

us_checkin = get_country_data(checkin_country, df_cities, country_code = 'US')
us_checkin.to_csv("us_checkin.csv")

jp_checkin = get_country_data(checkin_country, df_cities, country_code = 'JP')
jp_checkin.to_csv("jp_checkin.csv")
