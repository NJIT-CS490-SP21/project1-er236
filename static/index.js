var mainDiv;
var Lookup;
var searchDiv;
var lyrics;
var audio;
var audioSource
window.onload = (event) => {
    mainDiv=document.getElementById("main");
    Lookup=document.getElementById("search");
    searchDiv=document.getElementById("searchItems");
    audio=document.getElementById("audio");
    audioSource=document.getElementById("audioSource");
};
function search(){
    var data=JSON.stringify({
        "q":Lookup.value
    });
    fetch("/genius",{
        method: "POST",
        body:data
        
    })
    .then(reply=>reply.json())
    .then(response=>{
        searchDiv.innerHTML="";
        searchDiv.style.display="block";
        response["response"]["hits"].map(item=>{
            var main = document.createElement("div");
            main.classList.add("searchItem");
            
            var title=document.createElement("div");
            title.classList.add("Search_Title")
            title.innerHTML=item["result"]["title"]+ " by "+item["result"]["primary_artist"]["name"]

            var image=document.createElement("img");
            image.classList.add("searchItemsImage");
            image.src=item["result"]["song_art_image_url"];
            main.onclick=()=>{
                searchDiv.style.display="none";
                var lyric_content=item["embed_content"];
                var artist=item["result"]["primary_artist"]["name"];
                var song_image_url=item["result"]["song_art_image_url"];
                var song_title = item["result"]["title"];
                stuff(lyric_content,artist,song_image_url,song_title);
               
            }
            
            main.appendChild(image);
            main.appendChild(title);
            searchDiv.appendChild(main);
        })
    })
}
function stuff(lyric_content,artist,song_image_url,song_title){
    var data=JSON.stringify({
            "artist":artist,
            "song_title":song_title
    })
    fetch("/spotify",{
        method: "POST",
        body: data
        
    })
    .then(reply=>reply.json())
    .then(response=>{
        mainDiv.innerHTML="";
        for (const index in response){
            var track=response[index];
            
            var main = document.createElement("div");
            main.classList.add("track");
            
            var img=document.createElement("img");
            img.classList.add("song_image");
            img.src=song_image_url;
            
            var title=document.createElement("div");
            title.classList.add("title");
            title.innerHTML=track["name"] +" by " + track["artists"].map(artist=>{
                return artist["name"];
            });

            var lyric=document.createElement("div");
            lyric.classList.add("lyric_Link");
            lyric.innerHTML=lyric_content;
            lyric.children[0].children[0].target="_blank";

            var music=document.createElement("audio");
            music.classList.add("audio");
            music.controls = true;


            
            var musicSource=document.createElement("source");
            musicSource.src=track["preview_url"];
            music.appendChild(musicSource)

            
            
            
            main.appendChild(title);
            main.appendChild(img);
            main.appendChild(music);
            main.appendChild(lyric);
            mainDiv.appendChild(main)
        }
    })
}

