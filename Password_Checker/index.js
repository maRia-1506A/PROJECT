//1. import module
import express from "express";
import bodyParser from "body-parser";
import {dirname} from "path";
import { fileURLToPath } from "url";

//2. set dir name
const __dirname= dirname(fileURLToPath(import.meta.url));

//3. create express app and port
const app= express();
const port= 3000;

//8. variable to check user
var userAuthorization= false;

//4. middleware to parse from data
app.use(bodyParser.urlencoded({extended: true}));

//7. custome middleware function  to check
function passwordChecker(req, res, next) {
    const password= req.body["password"];
    if(password === "m@riA1506"){
        userAuthorization= true;
    }
    next();
}

//6. route for homepage
app.get("/", (req, res)=>{
    res.sendFile(__dirname+"/public/index.html");
});

//9. route to another page & check
app.post("/check", passwordChecker, (req, res)=>{
    if(userAuthorization) {
        res.sendFile(__dirname+"/public/secret.html");
    } else {
        res.sendFile(__dirname+"/public/index.html");
        //Alternatively res.redirect("/");
    }
});

//5. start server
app.listen(port, ()=>{
    console.log(`Server running on port ${port}`);
    
});

