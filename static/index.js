const search=()=>{
    fetch("https://cd8b221068af435fb1bc75eb15bcba3b.vfs.cloud9.us-east-1.amazonaws.com/spotify")
    .then(reply=>reply.json())
    .then(response=>{
        console.log(response)
    })
}