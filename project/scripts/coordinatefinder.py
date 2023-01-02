import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import requests
df = pd.read_csv('./project/data/ufo_clean.csv', low_memory=False)

import requests
import json
import time
from tqdm import tqdm

# import api key from secrets.json
api_key = json.load(open('./project/notebooks/secrets.json'))['google_maps_api_key']

def get_elevations(coordinates, API_KEY, rate_limit=10, batch_size=100, df=None):

    # only keep the coordinates that don't have an elevation already in the dataframe
    if df is not None:
        try:
            coordinates = [c for c in coordinates if pd.isnull(df.loc[(df['latitude'] == float(c.split(',')[0])) & (df['longitude'] == float(c.split(',')[1])), 'elevation'])]
        except:
            pass

    # coordinates must be in the format "lat,lng" or "lat,lng|lat,lng|lat,lng" etc.
    coordinates = [c for c in coordinates if len(c.split(',')) == 2] # remove any coordinates that don't have a lat and a long separated by a comma
    coordinates = [c for c in coordinates if c.split(',')[0] != 'nan'] # remove any coordinates that have a NaN for the latitude
    coordinates = [c for c in coordinates if c.split(',')[1] != 'nan'] # remove any coordinates that have a NaN for the longitude
    coordinates = [c for c in coordinates if c.split(',')[0] != ''] # remove any coordinates that have an empty string for the latitude
    coordinates = [c for c in coordinates if c.split(',')[1] != ''] # remove any coordinates that have an empty string for the longitude


    # loop through the batch strings and make the API calls
    for i in range(0, len(coordinates), 10):
        # make the API call
        url = f"https://maps.googleapis.com/maps/api/elevation/json?locations={','.join(coordinates[i:i+batch_size])}&key={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200: # if the request was successful
            data = response.json() # get the data
            this_location = data['results'][0]['location'] # get the location of the first result
            this_elevation= data['results'][0]['elevation'] # get the elevation of the first result
            # add the elevation to the dataframe if it was passed in as an argument to the function. Otherwise, just print it.
            if df is not None:
                df.loc[(df['latitude'] == this_location['lat']) & (df['longitude'] == this_location['lng']), 'elevation'] = this_elevation
            else:
                print(f"The elevation of the location is {this_elevation} meters")
            # save the dataframe to a csv
            df.to_csv('ufo_clean.csv', index=False)
            time.sleep(1/rate_limit)
        else:
            print("Something went wrong")
            # save the elevations to a csv with the coordinates
            df.to_csv('ufo_clean.csv', index=False)

# apply get_elevations to the lat/long columns of the dataframe

# make a column for the elevation full of NaNs if there is no elevation column already
if 'elevation' not in df.columns:
    df['elevation'] = np.nan
    # save the dataframe to a csv
    df.to_csv('ufo_clean.csv', index=False)

# get the elevations for the coordinates that don't have them
get_elevations(df[['latitude', 'longitude']].astype(str).apply(lambda x: ','.join(x), axis=1).tolist(), api_key, df=df)
# save the dataframe to a csv
df.to_csv('ufo_clean.csv', index=False)
