#import	random
import	pandas as pd
#import	numpy as np
from chooseArtist.chooseArtistFunction import *

artists = [['souly', 'hype', 'german', 'new sound'],
		  ['radiohead', 'old', 'tiktok', 'melancholic'],
		  ['Frank Ocean', 'slow', '2016', 'sommer'],
		  ['Whirr', 'slow', 'trending', 'shoegaze']]
artistDataFrame = pd.DataFrame(artists, columns = ['artist name', 'mood', 'genre', 'quality'])
#print(artist_df.iloc[1,0])
chooseArtist(artistDataFrame)
