from flask  import render_template, Flask, request
import os
from config import spotify,genius, getSpotifyToken
import json 

app=Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True



@app.route('/spotify',methods=['POST'])
def display():
    req=json.loads(request.data.decode())
    return(spotify(req))
    
    
@app.route('/genius',methods=['POST'])
def look():
    req= json.loads(request.data.decode())['q']
    return(genius(req))
    
    
@app.route('/')
def main():
    return render_template("index.html")
#set spotify Access token
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
