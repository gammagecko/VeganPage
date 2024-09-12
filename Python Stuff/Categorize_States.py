import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

# Load the shapefile of the US state boundaries.
# Replace 'path_to_shapefile' with the actual file path to your shapefile.
us_states = gpd.read_file("tl_2023_us_state.shp")
cols = ["Latitude", "Longitude", "name", "description"]
ARO = pd.read_csv("animalrightsmap_org.csv", usecols=cols)

def get_state_for_point(latitude, longitude):
    point = Point(longitude, latitude)
    for state in us_states.itertuples():
        if state.geometry.contains(point):
            return state.NAME  # Assuming 'NAME' is the column with state names.
    return None

ARO['State'] = ""
row_num = 0
for row in ARO.itertuples(index=True, name='Pandas'):
    state = get_state_for_point(row.Latitude, row.Longitude)
    ARO.at[row_num, 'State'] = state
    row_num += 1

ARO_USA = ARO.dropna(subset=['State'])
ARO_USA.to_csv("AnimalRightsOrgsUSA.csv")
