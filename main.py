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

#Get XML name
playlist = tm.xml_name()

#Get song list
song_list= []
song_list= tm.song_list_generator(playlist)

#Get artist list
artist_list=[]
artist_list=tm.artist_list_generator(playlist)

#Get album list 
album_list=[]
album_list=tm.album_list_generator(playlist)

#Get username
my_username = tm.get_username()

#Get playlist name 
playlist_name = tm.get_playlist_name()

#Create playlist
my_playlist_id = tm.create_playlist(my_username, playlist_name)

#Track ID List
track_id_list=[]

#Add songs to a playlist
tm.add_to_playlist(song_list, artist_list, album_list, my_username, my_playlist_id, track_id_list)

tm.everything(playlist, my_username, playlist_name)