import requests
import os
from dotenv import load_dotenv
import base64

load_dotenv()

def spotify():

    response=requests.post(
       "https://accounts.spotify.com/api/token",
       data={
           "grant_type":"client_credentials",
       },
       
       headers={
          "Authorization":"Basic %s" %  base64.b64encode((os.getenv("api_id")+":"+os.getenv("api_secret")).encode()).decode(),
          "Content-Type": "application/x-www-form-urlencoded"
       }
    ).json()

    songs=requests.get(
       "https://api.spotify.com/v1/browse/new-releases",
       params={
          "limit":10
       },
       headers={
          "Authorization":"Bearer "+ response["access_token"]
       }
   
    ).json()
    return (songs)
   
   
   
def genius():
    print("genius")