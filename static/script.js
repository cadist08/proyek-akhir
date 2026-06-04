window.onload = function(){

    fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:"start"
        })
    })
    .then(res=>res.json())
    .then(data=>{
        addBot(data.reply)
    })
}

function addUser(text){

    let box=document.getElementById("chat-box");

    box.innerHTML+=`
        <div class="message user">
            ${text}
        </div>
    `;
}

function addBot(text){

    let box=document.getElementById("chat-box");

    box.innerHTML+=`
        <div class="message bot">
            ${text}
        </div>
    `;

    box.scrollTop=box.scrollHeight;
}

function sendMessage(){

    let input=document.getElementById("message");

    let msg=input.value;

    if(msg==="") return;

    addUser(msg);

    fetch("/chat",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:msg
        })
    })
    .then(res=>res.json())
    .then(data=>{
        addBot(data.reply)
    })

    input.value="";
}