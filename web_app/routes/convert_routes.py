#this is the AppleMusicToSpotify/web_app/routes/convert_route.py file...

from flask import Blueprint, request, render_template, redirect, flash

from tajMusic import get_username, create_playlist, get_missing_track_id, add_songs_to_playlist, add_song_ids, add_to_playlist, song_list_generator, artist_list_generator, album_list_generator

convert_routes = Blueprint("convert_routes", __name__)

@convert_routes.route("/convert/playlist", methods=["POST"])
def convert_playlist():
    print("New Method")
  #  if request.method == "POST":
    request_data = dict(request.form)
    #request_files = dict(request.files)
    print("FORM DATA:", request_data)

    name = request_data.get("name") or "Taj on Aux"
    #put this in a .env
    username = request_data.get("username") or "31kxkygp247mvkk3ixeeiryzuodm"
    XML = request.files["XML"].filename or "Music.xml"

    try:
        song_l = song_list_generator(XML)
        artist_l = artist_list_generator(XML)
        album_l = album_list_generator(XML)
        track_i = []

        playlist_id = create_playlist(username, name)
        track_id = add_to_playlist(song_l, artist_l, album_l, username, playlist_id, track_i)

        #print(f.read())
        #return(username=username)
        #print(username)
        #print(name)
        #print(XML)
        #return("OPEN")
        return render_template("playlist.html",
            username=username, name=name)
        
    except Exception as err:
        print("OOps")
        return redirect("/convert")