import requests
import os
from dotenv import load_dotenv
import base64


load_dotenv()

spotify_token=""
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
def spotify():
    getSpotifyToken()
    
    artist_id="spotify:artist:1Xyo4u8uXC1ZmMpatF05PJ".split(":")[2]


    songs=requests.get(
       "https://api.spotify.com/v1/artists/"+artist_id+"/top-tracks",
       params={
          "market":"US"
       },
       headers={
          "Authorization":"Bearer "+ spotify_token
       }
   
    ).json()
    print(len(songs["tracks"]))
    for index in range(len(songs["tracks"])):
        # TODO: write code... in songs["tracks"]:
        songInfo=requests.get(
            "https://api.spotify.com/v1/tracks/"+songs["tracks"][index]["id"],
            params={
                "market":"US"
            }
            ,
            headers={
                "Authorization":"Bearer "+ spotify_token
            }
        ).json()
        
        songs["tracks"][index]["images"]=songInfo["album"]["images"]
    return (songs)
   

def genius():
    token=requests.get(
       "https://api.genius.com/oauth/authorize",
       params={
            "client_id":os.getenv("genius_id"),
            "redirect_uri":"https://cd8b221068af435fb1bc75eb15bcba3b.vfs.cloud9.us-east-1.amazonaws.com/",
            "scope":"me",
            "state":"",
            "response_type":"code"
       }
    )
    
   # print(token.content)