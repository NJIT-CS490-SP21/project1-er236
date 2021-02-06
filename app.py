import flask
import os
import random
from dotenv import load_dotenv
import base64
from config import spotify,genius, getSpotifyToken

app=flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/spotify')
def spotify_request():
    return (spotify())
@app.route('/')
def main():
    #return "hello world"

    genius()
    return flask.render_template("index.html")
#set spotify Access token
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
