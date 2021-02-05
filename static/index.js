var mainDiv;
window.onload = (event) => {
  mainDiv=document.getElementById("main");

};
function search(){
    fetch("https://cd8b221068af435fb1bc75eb15bcba3b.vfs.cloud9.us-east-1.amazonaws.com/spotify")
    .then(reply=>reply.json())
    .then(response=>{
        response["albums"]["items"].map(item=>{
            //console.log(item);
            var main = document.createElement("div");
            var title=document.createElement("div");
            var img = document.createElement("img");
            main.classList.add("item");
            title.classList.add("title");
            img.classList.add("img");
            console.log(item)
            title.innerHTML=item["name"]+" by "+item["artists"].map(artist=>{
                return " "+artist["name"]
            });
            img.src = item["images"][0]["url"]; 
            main.appendChild(title);
            main.appendChild(img);
            mainDiv.appendChild(main)
        })
    })
}