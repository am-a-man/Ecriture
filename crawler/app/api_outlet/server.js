

const express = require('express');
var app = express();
const fs = require('fs');
const { Z_FIXED } = require('zlib');

app.listen(8000, ()=>{
    console.log("listening at port: 8000, check at localhost:5000");
});


app.get("/working/:link", (request, response)=>{
    console.log("request recieved");
    var spawn = require("child_process").execSync;
    var link = (request.params.link);
    console.log(link);
    var process = spawn("python3 ./app/source.py link");


    file = fs.readFileSync("./api_outlet/content.txt");
    
    try {
        response.send(file.toString());
    } catch (error) {
        response.send(JSON.stringify({
            "status":String(error)
        }));
    }

});

