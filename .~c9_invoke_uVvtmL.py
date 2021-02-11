import requests
import os
from dotenv import load_dotenv
import base64
import json 

load_dotenv()

spotify_token=""


def genius(req):
    song=requests.get(
        "https://api.genius.com/search?q="+req,
        headers={
            "Authorization": "Bearer "+os.getenv("genius_token")
        }
    ).json()
    print(len(song["response"]["hits"]))
    for index in range(len(song["response"]["hits"])):
        track=song["response"]["hits"][index]
        lyric=requests.get(
            "https://api.genius.com/songs/"+str(track["result"]["id"]),
            headers={
                "Authorization": "Bearer "+os.getenv("genius_token")
            }
        ).json()
        print(lyric["response"]["song"])
        break
    return (song)


def getSpotifyToken():
    global spotify_token
    response=requests.post(
       "https://accounts.spotify.com/api/token",
       data={
           "grant_type":"client_credentials",
       },
       
       headers={
          "Authorization":"Basic %s" %  base64.b64encode((os.getenv("spotify_id")+":"+os.getenv("spotify_secret")).encode()).decode(),
          "Content-Type": "application/x-www-form-urlencoded"
       }
    ).json()

    spotify_token=response["access_token"]
def spotify(req):
    getSpotifyToken()
    artists=requests.get(
       "https://api.spotify.com/v1/search",
       params={
          "market":"US",
          "q":req["artist"],
          "type": "artist"
       },
       headers={
          "Authorization":"Bearer "+ spotify_token
       }
   
    ).json()
    artist_id=""
    for artist in artists["artists"]["items"]:
        if artist["name"]==req["artist"]:
            artist_id=artist["id"]
            
    songs=requests.get(
       "https://api.spotify.com/v1/search",
       params={
          "q":req["song_title"],
          "type": "track"
       },
       headers={
          "Authorization":"Bearer "+ spotify_token
       }
   
    ).json()
    song_ids={}
    for song in songs["tracks"]["items"]:
        for artist in song["artists"]:
            if artist_id==artist["id"] and req["song_title"] in song["name"]:
                song_ids[len(song_ids.keys())]=song
    
    return (song_ids)
    
   

