const express=require("express");
const router=express.Router()
const json=require("json")
const sql=require("mysql")
const db=require('./sqql')
router.get("/details",(req,res)=>{
    db.query("SELECT * FROM student",(err,rows,field)=>{
        if(!err){
            res.send(rows);
        }
        else
        console.log(err);
    })
});

router.delete("/details/:id",(req,res)=>{
    db.query("DELETE FROM student WHERE id = ?",req.params.id,(err,rows,field)=>{
        if(!err){
            res.send("DELETED");
        }
        else
        console.log(err);
    })
});
router.post("/login",(req,res)=>{
    const valu=req.body
    
    db.query("INSERT INTO student set ?",valu,(err,rows)=>{
        if(!err){
            res.send("inserted");
            console.log(valu);
        }
        else
        console.log(err);
    })
});


module.exports=router 