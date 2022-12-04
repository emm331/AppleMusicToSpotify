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

#Get username
my_username = tm.get_username()

#Create playlist
playlist_name = input('enter playlist name')
my_playlist_id = tm.create_playlist(my_username)

#Make track ID List 
song_list = []
artist_list = []
album_list = []

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
        artist_list.append(df['string'][i][0])
        print(df['string'][i][1])

#Album Name
with open(playlist) as fd:
    doc = xmltodict.parse(fd.read())
    df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
    for i in range(len(df)):
        album_list.append(df['string'][i][0])
        print(df['string'][i][4])

#Add songs to a playlist
token = util.prompt_for_user_token(username=my_username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        results = sp.user_playlist_add_tracks(my_username, playlist_name, song_list)
        print('Finished transferring playlist')
        #return results


#song_name = axp.get_song_name()
#final_song_name = axp.remove_feat_from_song(song_name)
#artist_name = axp.get_artist_name()
#album_name = axp.get_album_name()
#final_album_name = axp.remove_feat_from_album(album_name)
#my_playlist_id = sa.create_playlist(my_username)
#multiple_tracks, missing_albums, missing_tracks = sa.get_track_id(final_song_name, artist_name, final_album_name)
#more_tracks = sa.get_missing_track_id(missing_albums, missing_tracks)
#all_songs = sa.add_song_ids(multiple_tracks, more_tracks)
# sa.add_more_than_100_songs_to_playlist(my_username, my_playlist_id, all_songs)