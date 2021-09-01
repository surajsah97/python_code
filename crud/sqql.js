const mysql=require("mysql");
const createsqql=mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Surajsah@97",
    database:"suraj",
    multipleStatements:true
})
createsqql.connect((err)=>{
    if(!err){console.log('connected')}
    else{console.log('connection failed')}
    });
module.exports=createsqql;