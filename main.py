##import applemusic_xml_parser as axp
import tajMusic as tm
from bs4 import BeautifulSoup
import json
import xmltodict
import pprint
import pandas as pd

#New imports -- make sure to add these to requirements.txt
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import numpy as np

# Spotify Token Access
client_id = "e511d6d85faa4eb2bf5992529106c09b"
client_secret = "7ea0c0a57a434e6e915f683a8be4b920"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Greet user 
print('Welcome to Taj!\n')
playlist = input('Enter the XML file name: ') + '.xml'

#Make track ID List 
song_list = []
artist_list = []
album_list = []
track_id_list = []

#Song Name
with open(playlist) as fd:
    doc = xmltodict.parse(fd.read())
    df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
    for i in range(len(df)):
        song_list.append(df['string'][i][0])
        print(df['string'][i][0])

#Artist Name
with open(playlist) as fd:
    doc = xmltodict.parse(fd.read())
    df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
    for i in range(len(df)):
        artist_list.append(df['string'][i][1])
        print(df['string'][i][1])

#Album Name
with open(playlist) as fd:
    doc = xmltodict.parse(fd.read())
    df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
    for i in range(len(df)):
        album_list.append(df['string'][i][4])
        print(df['string'][i][4])

#Get username
my_username = tm.get_username()

#Create playlist
my_playlist_id = tm.create_playlist(my_username)

#Add songs to a playlist
tm.add_to_playlist(song_list, artist_list, album_list, my_username, my_playlist_id, track_id_list)

#for i in range(len(song_list)):
 #   track_dict = sp.search(q= song_list[i] + " " + artist_list[i] + " " + album_list[i], limit = 1, offset = 0, type='track', market=None)
  #  print(song_list[i] + " " + artist_list[i] + " " + album_list[i])

   # track_df = pd.DataFrame(track_dict['tracks']['items'])
    #track_id_list.append(track_df['id'])
#print(track_id_list)

#for i in range(len(track_id_list)):
#    token = tm.add_songs_to_playlist(my_username, my_playlist_id, track_id_list[i])