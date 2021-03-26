"""
Assignment #7: AJAX
"""

from flask import Flask, request, g
import json
import math

app = Flask(__name__)


class Albums():
    """Class representing a collection of albums."""

    def __init__(self, albums_file, tracks_file):
        self.__albums = {}
        self.__load_albums(albums_file)
        self.__load_tracks(tracks_file)

    def __load_albums(self, albums_file):
        """Loads a list of albums from a file."""
        with open(albums_file) as fil:
            for linje in fil:
                print(linje)
                album_id, artist, title, cover_img = linje.strip().split("\t")
                self.__albums[album_id] = {
                    "artist": artist,
                    "title": title,
                    "cover_img": cover_img,
                    "tracks": []
                }

    def __load_tracks(self, tracks_file):
        """Loads a list of tracks from a file."""
        with open(tracks_file) as fil:
            for linje in fil:
                album_id, title, length = linje.strip().split("\t")
                self.__albums[album_id]["tracks"].append({
                    "title": title,
                    "length": length
                })

    def get_albums(self):
        """Returns a list of all albums, with album_id, artist and title."""
        all = []
        for album_id, contents in self.__albums.items():
            all.append({
                "album_id": album_id,
                "artist": contents["artist"],
                "title": contents["title"]
            })
        return all

    def get_album(self, album_id):
        """Returns all details of an album."""
        album = self.__albums.get(album_id, None)
        if album:
            lengde = 0

            for track in album["tracks"]:
                m, s = track["length"].split(":")
                lengde += 60 * int(m) + int(s)
            album["length"] = "{:02d}:{:02d}".format(math.floor(lengde / 60), lengde % 60)
        return album


# the Albums class is instantiated and stored in a config variable
# it's not the cleanest thing ever, but makes sure that the we load the text files only once
app.config["albums"] = Albums("data/albums.txt", "data/tracks.txt")


@app.route("/albums")
def albums():
    """Returns a list of albums (with album_id, author, and title) in JSON."""
    albums = app.config["albums"]
    return json.dumps(albums.get_albums())


@app.route("/albuminfo")
def albuminfo():
    albums = app.config["albums"]
    album_id = request.args.get("album_id", None)
    if album_id:
        return json.dumps(albums.get_album(album_id))
    return ""


@app.route("/sample")
def sample():
    return app.send_static_file("index_static.html")


@app.route("/")
def index():
    return app.send_static_file("index.html")


if __name__ == "__main__":
    app.run()
