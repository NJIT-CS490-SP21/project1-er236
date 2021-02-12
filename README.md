# Song Searcher
a web application that let's users search lyrics and shows song results. The user can then click on the song to view information. 
This information include a song preview, the name of the song, the artist, a song related image, and a link to the lyrics of the song.

## Technologies used
1. Python
2. Flask
3. HTML/CSS
4. Javascript

## APIs
1. Spotify API
2. Genius API


## How to use Application
1. Run "pip install Flask python-dotenv requests" in command
2. Then run the app.py 
3. Make an .env files and insert spotify id,secret and redirect url, and the genius api access token
3. Open app in browser
4. Search lyric in search bar and then click search button
5. Once results show up click on one and spotify result for that item will be shown



## Three least technical issues you encountered with in my project and How I fixed them
1. One of my techical issues was aligning my items with css. With some research and testing out different css attributes I more or less fixed it.
2. Another issue was showing json on python. Since it wasnt parsed, I'd have to send it to my browser
   to see how it looked before returning to python use it correctly.
3. Another technical issue was starting to use APIs. Took some researching and trial and error to see how to
   correctly send data to the APIs.

## What would I do to imporve the project in the future?
1. Store search data to decrease API calls and response to users faster.
2. change search event to onchange so make it look more cooler
