##import applemusic_xml_parser as axp
import tajMusic as tm
from bs4 import BeautifulSoup
import json
import xmltodict
import pprint

#Greet user 
print('Welcome to Taj!\n')
playlist = input('Enter the XML file name: ') + '.xml'

#Get username
my_username = tm.get_username()

print(playlist)

with open(playlist) as fd:
    doc = xmltodict.parse(fd.read())

#print(doc)
#print("The type is", type(doc))
print(doc['plist']['@version'])

#pp = pprint.PrettyPrinter(indent = 4)
#pp.pprint(json.dumps(doc))

##print("nw") my_dict = xmltodict.parse(doc)
#print(my_dict['Name'])
    
#convert xml to dict
#newdict = dict2xml(playlist, wrap ='root', indent = "    ")
#print(newdict)
#dictionary = BeautifulSoup(open(playlist), 'xml')
#print(dictionary.keys())
#print(dictionary)
#x = dictionary.keys()

#print(list(dict.keys())[list(dict.values()).index(16)]) x = dictionary.items("Track ID")

#print(xml_parser)
#print(xml_parser["Delicate"])

#songname = xml_parser.find('Delicate')

#for key, value in tm.xml_parser():
 #   print(key, '->', value)

#print(songname)


#Name playlist


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