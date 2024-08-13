import datetime
import os

import os
import time
from pprint import pprint

os.environ["SPOTIPY_CLIENT_ID"] = "SPOTIPY_CLIENT_ID"
os.environ["SPOTIPY_CLIENT_SECRET"] = "SPOTIPY_CLIENT_SECRET"
os.environ["SPOTIPY_REDIRECT_URI"] = "SPOTIPY_REDIRECT_URI"

from dotenv import load_dotenv

import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
response = requests.get(f"https://www.billboard.com/charts/hot-100/2000-08-12/")

soup = BeautifulSoup(response.text, "html.parser")

songs_name = [str.replace(str.replace(title.getText(), '\n', ''), '\t', '') for title
              in soup.select(selector="ul li h3.c-title")]

print(songs_name)

scope = "user-library-read playlist-modify-public playlist-read-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.environ.get("SPOTIPY_REDIRECT_URI"),
    scope=scope))

results = sp.current_user()
user_id = results["id"]
date = datetime.datetime(2000, 8, 12)
year = datetime.datetime.strftime(date, '%y')

spotify_uris = []

for song in songs_name:
    try:
        result = sp.search(q=f"track:{song}", limit=1, type="track")
        spotify_uris.append(result["tracks"]["items"][0]["uri"])
    except:
        pass


playlist_name = f"{datetime.datetime.strftime(date, '%Y-%m-%d')} Billboard 100"

user_playlists = sp.user_playlists(user_id)

playlist_id = ''

for playlist in user_playlists["items"]:
    if playlist["name"] == playlist_name:
        playlist_id = playlist["id"]
        break

if playlist_id == '' or playlist_id is None:
    playlist = sp.user_playlist_create(user=user_id,
                                       name=playlist_name,
                                       public=True,
                                       description='Teste')
    playlist_id = playlist["id"]

print(playlist_id)

tracksin = sp.playlist_items(playlist_id)

playlist_songs = [items["track"]["uri"] for items in tracksin["items"]]

uris_to_add = list(set(spotify_uris).difference(playlist_songs))

if len(uris_to_add) > 0:
    response = sp.playlist_add_items(playlist_id, uris_to_add)
