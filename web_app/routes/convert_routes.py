#this is the AppleMusicToSpotify/web_app/routes/convert_route.py file...

from flask import Blueprint, request, render_template, redirect, flash

from tajMusic import get_username, create_playlist, get_missing_track_id, add_songs_to_playlist, add_song_ids, add_to_playlist

convert_routes = Blueprint("convert_routes", __name__)

@convert_routes.route("/convert/playlist", methods=["POST"])
def convert_playlist():
    print("New Method")

  #  if request.method == "POST":
    request_data = dict(request.form)
    request_file = dict(request.files)
    print("FORM DATA:", request_data)

    name = request_data.get("name") or "Taj on Aux"
    #put this in a .env
    username = request_data.get("username") or "31kxkygp247mvkk3ixeeiryzuodm"
    XML = request_file.get("XML") or "Music"

    try:
        df = everything(XML=XML, name=name, username=username)
        return("OPEN")
        
    except Exception as err:
        print("OOps")
        return redirect("/convert")