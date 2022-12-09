##import applemusic_xml_parser as axp
from bs4 import BeautifulSoup
import json
import xmltodict
import pprint
import pandas as pd

from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import spotipy.util as util
import numpy as np

# Spotify Token Access
#Do we need this here, i think we have it in main
client_id = "e511d6d85faa4eb2bf5992529106c09b"
client_secret = "7ea0c0a57a434e6e915f683a8be4b920"
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

song_list=[]
# Get Spotify Username
def get_username():
    username = input('Enter Username: ')
    print(username)
    check = input('Is this your username? (Y/N): ')
    if check.upper() == 'Y':
        return username
    else:
        new_username = input('Reenter Username: ')
        return new_username

def xml_name():
    #Greet user 
    print('Welcome to Taj!\n')
    playlist = input('Enter the XML file name: ') + '.xml'
    return playlist

#Get playlist name
def get_playlist_name():
    playlist_name= input("Enter a playlist name: ")
    return playlist_name

def song_list_generator(playlist):
    #Make track ID List 
   
    song_list = []
    #Song Name
    with open(playlist) as fd:
        doc = xmltodict.parse(fd.read())
        df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
        for i in range(len(df)):
            song_list.append(df['string'][i][0])
            print(df['string'][i][0])
    return song_list

def artist_list_generator(playlist):
    #Artist Name
    artist_list = []
    with open(playlist) as fd:
        doc = xmltodict.parse(fd.read())
        df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
        for i in range(len(df)):
            artist_list.append(df['string'][i][1])
            print(df['string'][i][1])
    return artist_list

def album_list_generator(playlist):
    #Album Name
    album_list = []
    with open(playlist) as fd:
        doc = xmltodict.parse(fd.read())
        df = pd.DataFrame(doc['plist']['dict']['dict']['dict'])
        for i in range(len(df)):
            album_list.append(df['string'][i][4])
            print(df['string'][i][4])
    return album_list

#Create Spotify playlist ID
def create_playlist(username, playlist_name):
    track_id_list = []
    username = username
   # playlist_name = input('Enter playlist name: ')

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        playlists = sp.user_playlist_create(username, playlist_name)
        return playlists['id']
    
# Get trackID for songs
def get_missing_track_id(missing_albums1, missing_tracks1):
    id_list = []
    my_array = []

    i = 0
    while i < len(missing_tracks1):
        album = missing_albums1[i]
        track = missing_tracks1[i]

        track_id = sp.search(q='album:' + album + ' track:' + track, type='track')
        for songsID in track_id['tracks']['items']:
            id_list.append(songsID['id'])
        if not id_list:
            print('Could not add: ' + missing_tracks1[i])
        else:
            my_array.append(id_list[0])
        id_list = []
        i += 1
    return my_array

# Add songs to Spotify Playlist
def add_songs_to_playlist(username, playlist_id, track_ids):
    
    username = username
    playlist_id = playlist_id
    track_ids = track_ids

    token = util.prompt_for_user_token(username=username, scope='playlist-modify-public', client_id=client_id,
                                       client_secret=client_secret, redirect_uri="http://localhost:8888/callback")
    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False

        results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
        print('Finished transferring playlist')
        print(results)
        return results
    
def add_song_ids(multiple_tracks1, more_tracks1):
    result = multiple_tracks1 + more_tracks1
   # print("Song", result)
    return result

#Add songs to a playlist
def add_to_playlist(song_list, artist_list, album_list, my_username, my_playlist_id, track_id_list):
    for i in range(len(song_list)):
        track_dict = sp.search(q= song_list[i] + " " + artist_list[i] + " " + album_list[i], limit = 1, offset = 0, type='track', market=None)
        print(song_list[i] + " " + artist_list[i] + " " + album_list[i])

        track_df = pd.DataFrame(track_dict['tracks']['items'])
        track_id_list.append(track_df['id'])
    print(track_id_list)

    for i in range(len(track_id_list)):
        token = app.tm.add_songs_to_playlist(my_username, my_playlist_id, track_id_list[i])

