

const express = require('express');
var app = express();
const fs = require('fs');
const { Z_FIXED } = require('zlib');

app.listen(8000, ()=>{
    console.log("listening at port: 8000, check at localhost:5000");
});


app.get("/loaddata", async (request, response)=>{
    console.log("get request: loadData");
    var exec = require("child_process").execSync;

    var process = exec("python3 ./app/ms_bot.py");
    
    // console.log(process.toString());
    file = fs.readFileSync("./api_outlet/content.json");
    fs.writeFile("./api_outlet/logs", process.toString())
    try {
        response.send(JSON.parse(file));
    } catch (error) {
        response.send(JSON.stringify({
            "status":String(error)
        }));
    }

});



app.get("/data", (request, response)=>{
    console.log("get request: data");

    file = fs.readFileSync("./api_outlet/content.json");
    
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


