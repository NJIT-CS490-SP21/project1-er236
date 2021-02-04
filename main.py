import flask
import os
import random
from dotenv import load_dotenv
import base64


app=flask.Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
    #return "hello world"
    shows=["Community","Avatar","Magi","Adventure Time","Hell's Kitchen"]
    showsurl=["community.jpg","avatar.jpg","magi.jpg","adventuretime.jpg","hellskitchen.jpg"]
    random_number = random.randint(0,len(shows)-1)
    return flask.render_template("index.html",length=len(shows),shows=shows,showsurl=showsurl)
    
app.run(
    port=int(os.getenv('PORT',8080)),
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
