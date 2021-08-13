

const express = require('express');
var app = express();
const fs = require('fs');
const { Z_FIXED } = require('zlib');

app.listen(8000, ()=>{
    console.log("listening at port: 8000, check at localhost:5000");
});


app.get("/loaddata", async (request, response)=>{
    console.log("get request: loadData");
    var spawn = require("child_process").spawn;

    var process = spawn("python3", ["./app/main.py"], {stdio:"inherit"});

    var i =0;
    // process.stdout.on('data', data=>{
    //     console.log(data.toString());
    //     console.log(`->>>${i}`);
    //     i++;
    // });

    process.on('exit',(code)=>{
    // file = fs.readFileSync("./api_outlet/content.json");
    // try {
    //     response.send(JSON.parse(file));
    // } catch (error) {
    //     response.send(JSON.stringify({
    //         "status":String(error)
    //     }));
    // }
    // });
    console.log(`exited: ${code}`);
    file = fs.readFileSync("./server/api_outlet/content.json");
    try {
        response.send(JSON.parse(file));
    } catch (error) {
        response.send(JSON.stringify({
            "status":String(error)
        }));
    }
    });
});



app.get("/data", (request, response)=>{
    console.log("get request: data");

    file = fs.readFileSync("./server/api_outlet/content.json");
    
    try {
        response.send(JSON.parse(file));
    } catch (error) {   
        response.send(JSON.stringify({
            "status":String(error)
        }));
    }

});


app.post("/new-data", (request,response)=>{
    console.log("post request : new-data");;
});



