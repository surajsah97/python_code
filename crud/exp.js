const express=require("express");
const app=express()
const sql=require("mysql")
const sqql=require("./sqql");
const sqll = require('./sqll');
const router=require("./router")
app.use(express.json())
app.use("/",router)
app.listen(3000,()=>{
    
    console.log("listioning");
})