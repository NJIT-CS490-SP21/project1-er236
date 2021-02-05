var mainDiv;
window.onload = (event) => {
  mainDiv=document.getElementById("main");

};
function search(){
    fetch("/spotify")
    .then(reply=>reply.json())
    .then(response=>{
        response["albums"]["items"].map(item=>{
            //console.log(item);
            var main = document.createElement("div");
            main.classList.add("item");
            var header=document.createElement("div");
            header.classList.add("header");

            var title=document.createElement("a");
            title.innerHTML=item["name"];
            
            title.href=item["external_urls"]["spotify"];
            var img = document.createElement("img");
            img.classList.add("img");

            
           
            
            console.log(item)

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