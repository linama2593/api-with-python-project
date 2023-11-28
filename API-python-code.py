#pip install spotipy
#pip install python-dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import matplotlib.pyplot as plt
import pandas as pd
from dotenv import load_dotenv
import numpy as np

############# loading  the .env file variables################
load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

#################### Creating the Spotify client ####################
con = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))


################### Making the API request #######################

#Getting artist ID
fatima_id='6jZSXmTCxZhFfYELtp78Ci'

#importing songs
output=con.artist_top_tracks(fatima_id)

songs=[]
if output:
    for track in output['tracks']:
        tracks = {}
        tracks['name']=track['name']
        tracks['popularity']=track['popularity']
        tracks['duration']=track['duration_ms']/60000
        songs.append(tracks)

############### Creating DataFrame #############
songs_df=pd.DataFrame(songs)
songs_df


############# Plotting scatter plot ###########

# Create the trendline
coefficients = np.polyfit(songs_df['duration'], songs_df['popularity'], 1)  # Fit a first-degree (linear) polynomial
trendline = np.poly1d(coefficients)
y_fit = trendline(songs_df['duration'])

#Creating plot
plt.scatter(songs_df['duration'], songs_df['popularity'])
plt.plot(songs_df['duration'], y_fit, linestyle='--', color='red')
plt.title('Relationship between duration and popularity')
plt.xlabel('Song duration in minutes')
plt.ylabel('Popularity ranking')
plt.show()

print("""
Conclusion: There is a possitive association between
duration and popularity, based on the trendline.
However, given the few data points available, it is not possible to
determine whether this association is statistically significant.
Even if this association was statistically significant, correlation
is not causation. 
      """)