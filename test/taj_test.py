#put test functions
from app.tajMusic import song_list_generator, artist_list_generator, album_list_generator
import os

#Point to file, test directory, up 1 level to root directory to Music.xml
#Going to use Music.xml

xml_filepath = os.path.join(os.path.dirname(__file__), "..", "Music.xml") #come back to this

def test_xml_parse_artist():
    results = song_list_generator(xml_filepath)
   # breakpoint()
    assert results == ['Delicate', 'Look What You Made Me Do', 'I Did Something Bad', 'Don’t Blame Me', 'End Game (feat. Ed Sheeran & Future)', '...Ready For It?', 'Hope Will Lead Us On', 'Call It What You Want', 'Hold Up', 'New Year’s Day', 'Dress', 'This Is Why We Can’t Have Nice Things', 'King of My Heart', 'Dancing With Our Hands Tied', 'Gorgeous', 'Getaway Car', 'So It Goes...']
