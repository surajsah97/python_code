from flask import Flask, render_template, jsonify,request
import MySQLdb as mdb
app= Flask(__name__)
conn = mdb.connect('localhost', 'root', 'Surajsah@97', 'express')
cursor = conn.cursor()
@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/about')
def about():
    items="suraj"
    return render_template("about.html",item=items)
# @app.route('/about/<username>')
# def about(username):
#     return f"<h1>Hello,{username}</h1>"
@app.route('/register',methods=['POST', 'GET'])
def resister():
    if request.method=='GET':
        return 'hello register page'
    elif request.method == 'POST':
        name=request.json["name"]
        email=request.json["email"]
        password=request.json["password"]
        conf_password=request.json["confirm_password"]
        cursor.execute("SELECT * from user WHERE email LIKE %s",(email,))
        # cursor.execute("INSERT INTO user(name,email,password) VALUES(%s, %s, %s)",(name,email,password))
        rv = cursor.fetchall()
        if len(rv)<=0:
            cursor.execute("INSERT INTO user(name,email,password,confirm_password) VALUES(%s, %s, %s,%s)",(name,email,password,conf_password))
            cursor.close()
            conn.commit()
            conn.close()
            return "successfully registered"
        elif len(rv)>0:
            return "sorry already resistered"

@app.route('/login',methods=['POST', 'GET'])
def login():
    if request.method=='GET':
        return 'welcome to login'
    elif request.method == 'POST':
        email=request.json["email"]
        password=request.json["password"]
        cursor.execute("SELECT password from user WHERE email LIKE %s", (email,))#(('geudstu',),)
        rv = cursor.fetchall()
        if len(rv)>0:
            t=str(rv).replace("(","")
            d=t.replace(",)","")
            if "'"+password+"'"==d:
                cursor.close()
                conn.commit()
                conn.close()
                return "successfully logged"
                
            elif "'"+password+"'"!=d:
                return "sorry incorrect password"
        elif len(rv)<=0:
            return "you are not registerd wrong username"
        

if __name__ == "__main__":
    app.run(debug=True,port=8000)
    