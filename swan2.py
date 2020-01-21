from flask import Flask,render_template,flash, redirect,url_for,session,logging,request,jsonify
import json
import mysql.connector



app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")



@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]

        return json.dumps({'uname':uname})

        #login = user.query.filter_by(username=uname, password=passw).first()
        #if login is not None:
            #return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        mail = request.form['mail']
        passw = request.form['passw']
        mydb = mysql.connector.connect(
        host="10.14.79.58",
        user="root",
        passwd="12345",
        database="PATIENT")
 
        mycursor = mydb.cursor()

        PATIENT = "INSERT INTO PERSONAL_DETAILS (name, email,password) VALUES (%s, %s, %s)"
        val = (uname,mail,passw)
        mycursor.execute(PATIENT, val)

        mydb.commit()


        


        #register = user(username = uname, email = mail, password = passw)
        #db.session.add(register)
        #db.session.commit()

        #return redirect(url_for("login"))
    return render_template("register.html")

if __name__ == '__main__': 

	app.run(debug = True) 
