var mainDiv;
window.onload = (event) => {
  mainDiv=document.getElementById("main");

};
function search(){
    fetch("/spotify")
    .then(reply=>reply.json())
    .then(response=>{
        console.log(response);
        mainDiv.innerHTML="";
        response["tracks"].map(item=>{
            
            
            var main = document.createElement("div");
            main.classList.add("item");
            var header=document.createElement("div");
            header.classList.add("header");

            var title=document.createElement("a");
            title.innerHTML=item["name"];
            
            if (item["preview_url"]==null){
                title.href=item["external_urls"]["spotify"];

            }
            else{
                title.href=item["preview_url"];
            }
            var img = document.createElement("img");
            img.classList.add("img");

            
           
            
            img.src = item["images"][0]["url"]; 
            header.appendChild(title)
            header.innerHTML=header.innerHTML+" By: " +item["artists"].map(artist=>{
                return " "+artist["name"]
            });
            main.appendChild(header);
            main.appendChild(img);
            mainDiv.appendChild(main)
        })
    })
}