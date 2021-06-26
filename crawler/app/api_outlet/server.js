

const express = require('express')
var app = express()


app.listen(8000, ()=>{
    console.log("listening at port: 8000");
})


app.get("/working/:link",(request, response)=>{
    console.log("request recieved");
    var spawn = require("child_process").spawn;
    var link = (request.params.link);
    console.log(link);
try {
    var process = spawn("python3", ["source.py"]);

    process.stdout.on('data', function(data) {
        response.send(data.toString())});

    
} catch (error) {
    response.send(JSON.stringify({
        "status":String(error)
    }));
}



});

