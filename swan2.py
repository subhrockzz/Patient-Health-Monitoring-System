from flask import Flask,render_template,flash, redirect,url_for,session,logging,request,jsonify,Response
import json
import socket
import mysql.connector
import hashlib
import random
import time
import os
from datetime import datetime
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "Subhrajeet"
@app.route("/")
def frontpage():
    return render_template("frontpage.html")
@app.route("/offline",methods=["GET","POST"])
def offline(): 
    return render_template("offline.html")
@app.route("/reboot",methods=["GET","POST"])
def reboot():

    os.system("sudo reboot")
    return "null"
@app.route("/online",methods=["GET", "POST"])
def online():
    if request.method == "POST":
        graph_data = open("PERSONAL_INFO.txt",'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                mydb = mysql.connector.connect(
                host="10.14.79.58",
                user="root",
                passwd="12345",
                database="PATIENT")

                mycursor = mydb.cursor()
                utype,uname,mail,phn,gender,age,passw,fingerprint=line.split(',')
                hashkey=hash(uname+mail+phn)
                PATIENT = "INSERT INTO PATIENT_INFO (Hashkey,UserType,Name,Email,PhoneNo,Gender,Age,Password,Fingerprint) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (hashkey,utype,uname,mail,phn,gender,age,passw,fingerprint)
                mycursor.execute(PATIENT, val)

                mydb.commit()

                open("PERSONAL_INFO.txt", "w").close()

        mail = request.form["mail"]
        session['mail']=mail
        passw = request.form["passw"]
        mydb = mysql.connector.connect(
        host="10.14.79.58",
        user="root",
        passwd="12345",
        database="PATIENT")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM PATIENT_INFO WHERE Email = %s AND Password = %s', (mail, passw))
        # Fetch one record and return result
        account = mycursor.fetchone()
        mydb.commit()
        # If account exists in accounts table in out database
        if account:
            #flash('Logged in successfully.')

            # Create session data, we can access this data in other routes
            #session['loggedin'] = True
            #session["mail"] = account["Email"]
            mydb = mysql.connector.connect(
            host="10.14.79.58",
            user="root",
            passwd="12345",
            database="PATIENT")

            mycursor = mydb.cursor()
            mycursor.execute('SELECT Name FROM PATIENT_INFO WHERE Email = %s AND Password = %s', (mail, passw))
            #f.write("%s,%s,%s,%s,%s,%s,%s" % (utype,uname,mail,phn,gender,age,passw))

        # Fetch one record and return result
            name =str(mycursor.fetchone()[0])
            #age=str(mycursor.fetchone()[1]
            #gender=str(mycursor.fetchone()[2]
            #hashkey=str(mycursor.fetchone()[3]
            mydb.commit()
            mydb = mysql.connector.connect(
            host="10.14.79.58",
            user="root",
            passwd="12345",
            database="PATIENT")

            mycursor = mydb.cursor()
            mycursor.execute('SELECT Age FROM PATIENT_INFO WHERE Email = %s AND Password = %s', (mail, passw))
            age=str(mycursor.fetchone()[0])
            mydb.commit()
            mydb = mysql.connector.connect(
            host="10.14.79.58",
            user="root",
            passwd="12345",
            database="PATIENT")

            mycursor = mydb.cursor()
            mycursor.execute('SELECT Gender FROM PATIENT_INFO WHERE Email = %s AND Password = %s', (mail, passw))
            gender=str(mycursor.fetchone()[0])
            mydb.commit()
            #open("PERSONAL_INFO.txt", "w").close()
            #session['hashkey']=hashkey
            f= open("P_INFO.txt","w+")
            f.write("%s,%s" % (gender,age))

         
            # Redirect to home page

         
           # while(1):
        
                #mydb = mysql.connector.connect(
                #host="10.14.79.58",
                #user="root",
                #passwd="12345",
                #database="PATIENT")

                #mycursor = mydb.cursor()
                #hashkey="1234"
                #gender="Male"
                #age="25"
                #temp="98"
                #hr="72"
                #sys="67"
                #dia="90"
                #spo2="100"
                #ci='5'
                #PATIENT = "INSERT INTO MEDICAL_INFO (Hashkey,Gender,Age,Temperature,HeartRate,Systole,Diastole,Spo2,CriticalIndex) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
                #val = (hashkey,gender,age,temp,hr,sys,dia,spo2,ci)
                #mycursor.execute(PATIENT, val)

                #mydb.commit()



            return render_template('details.html',name=name)

        else:
            return render_template('register.html')

        #login = user.query.filter_by(username=uname, password=passw).first()
        #if login is not None:
            #return redirect(url_for("index"))
    return render_template("online.html")

@app.route("/offlinelogin",methods=["GET", "POST"])
def offlinelogin():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345",
        database="PATIENT")

        mycursor = mydb.cursor()
        mycursor.execute('SELECT * FROM PERSONAL_INFO WHERE Name = %s AND Password = %s', (uname, passw))
        # Fetch one record and return result
        account = mycursor.fetchone()
        mydb.commit()
        if account:
           # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['uname']
            session['username'] = account['passw']
           # Redirect to home page
            return render_template('offlinedetails.html')
        else:
            return render_template('offlineregister.html')

        #login = user.query.filter_by(username=uname, password=passw).first()
        #if login is not None:
            #return redirect(url_for("index"))
    return render_template("offlinelogin.html")






@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        graph_data = open('PERSONAL_INFO.txt','r').read()
        lines = graph_data.split('\n')
        data = open('F_LOGIN.txt','r').read()
        l = data.split('\n')
        for li in l:
            if len(li) >= 1:
        #x,y=line.split(',')
                x=li

        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                mydb = mysql.connector.connect(
                host="10.14.79.58",
                port='3306',
                user="root",
                passwd="12345",
                database="PATIENT")

                mycursor = mydb.cursor()
                utype,uname,mail,phn,gender,age,passw=line.split(',')
                #hashkey=hash(uname+mail+phn)
                y = hashlib.sha1(str.encode(mail))
                hashkey=str(y.hexdigest())
                PATIENT = "INSERT INTO PATIENT_INFO (Hashkey,UserType,Name,Email,PhoneNo,Gender,Age,Password,Fingerprint) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (hashkey,utype,uname,mail,phn,gender,age,passw,x)
                mycursor.execute(PATIENT, val)

                mydb.commit()

        open("PERSONAL_INFO.txt", "w").close()
        #open("F_ENROLL.txt","w").close()
        uname = request.form['uname']
        utype = request.form['utype']
        mail = request.form['mail']
        phn = request.form['phn']
        gender = request.form['gender']
        age = request.form['age']
        passw = request.form['passw']
        fp=open("F_ENROLL.txt",'r').read()
        #x = hashlib.sha1(str.encode(uname+gender+phn))
        session['mail']=mail
        #x = hashlib.sha1(str.encode(uname+gender+phn))
        y = hashlib.sha1(str.encode(mail))
        hashkey=str(y.hexdigest())
        #hashkey = x.hexdigest()
        f1= open("P_INFO.txt","w+")
        f1.write("%s,%s" % (gender,age))

        

       
        #hashkey = x.hexdigest()
        mydb = mysql.connector.connect(
        host="10.14.79.58",
        port='3306',
        user="root",
        passwd="12345",
        database="PATIENT")

        mycursor = mydb.cursor()

        PATIENT = "INSERT INTO PATIENT_INFO (Hashkey,UserType,Name,Email,PhoneNo,Gender,Age,Password,Fingerprint) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)"
        val = (hashkey,utype,uname,mail,phn,gender,age,passw,fp)
        mycursor.execute(PATIENT, val)

        mydb.commit()
        return render_template('details.html',name=uname)

    return render_template("register.html")
@app.route("/offlineregister", methods=["GET", "POST"])
def offlineregister():
    if request.method == "POST":
        uname = request.form['uname']
        utype = request.form['utype']
        mail = request.form['mail']
        phn = request.form['phn']
        gender = request.form['gender']
        age = request.form['age']
        passw = request.form['passw']
        session['mail']=mail
        #x = hashlib.sha1(str.encode(uname+gender+phn))
        hashkey=hash(uname+mail+phn)
        #hashkey = x.hexdigest()
        f= open("PERSONAL_INFO.txt","w+")
        f.write("%s,%s,%s,%s,%s,%s,%s" % (utype,uname,mail,phn,gender,age,passw))
        return render_template('offlinedetails.html',name=uname)

    return render_template("offlineregister.html")

@app.route("/details")
def details():
    #if 'mail' in session: 
        #email=session['mail']
        #mydb = mysql.connector.connect(
            #host="10.14.79.58",
            #user="root",
            #passwd="12345",
            #database="PATIENT")

        #mycursor = mydb.cursor()
        #mycursor.execute('SELECT Name FROM PATIENT_INFO WHERE Fingerprint= %s', (mail, passw))
        #name=str(mycursor.fetchone()[0])
        #mydb.commit()

    return render_template("details.html")
@app.route("/offlinedetails")
def offlinedetails():
    return render_template("offlinedetails.html")
@app.route("/start")
def start():
    if 'mail' in session: 
        email=session['mail']
    mydb = mysql.connector.connect(
    host="10.14.79.58",
    user="root",
    passwd="12345",
    database="PATIENT")

    mycursor = mydb.cursor()
    #print(session['mail'])
    mycursor.execute("SELECT Hashkey FROM PATIENT_INFO WHERE Email = '%s'"%email)
        # Fetch one record and return result
    hashkey = str(mycursor.fetchone()[0])
    mydb.commit()

    mydb = mysql.connector.connect(
    host="10.14.79.58",
    user="root",
    passwd="12345",
    database="PATIENT")

    mycursor = mydb.cursor()
    #print(session['mail']) 
    mycursor.execute("SELECT Age FROM PATIENT_INFO WHERE Email = '%s'"%email)
        # Fetch one record and return result
    age = str(mycursor.fetchone()[0])
    mydb.commit() 

    mydb = mysql.connector.connect(
    host="10.14.79.58",
    user="root",
    passwd="12345",
    database="PATIENT")

    mycursor = mydb.cursor()
    #print(session['mail']) 
    mycursor.execute("SELECT Gender FROM PATIENT_INFO WHERE Email = '%s'"%email)
        # Fetch one record and return result
    gender = str(mycursor.fetchone()[0])
  
    mydb.commit() 
 
    mydb = mysql.connector.connect(
    host="10.14.79.58",
    user="root",
    passwd="12345",
    database="PATIENT")

    mycursor = mydb.cursor()
    #print(session['mail']) 
    mycursor.execute("SELECT Name FROM PATIENT_INFO WHERE Email = '%s'"%email)
        # Fetch one record and return result
    name = str(mycursor.fetchone()[0])

    mydb.commit() 



    graph_data = open('spo2.txt','r').read()
    graph_data2 = open('BP.txt','r').read()
    graph_data3 = open('CI.txt','r').read()
    lines = graph_data.split('\n')
    lines2 = graph_data2.split('\n')
    lines3 = graph_data3.split('\n')
    xs = []
    ys = []
    i=0
    for line,line2,line3 in zip(lines,lines2,lines3):
        if len(line2) > 1:
            mydb = mysql.connector.connect(
            host="10.14.79.58",
            user="root",
            passwd="12345",
            database="PATIENT")

            mycursor = mydb.cursor()
            #sys,dia=line2.split(',')
            
           
            spo2,hr,temp=line.split(',')
            sys,dia=line2.split(',')
            ci=line3
            time=datetime.now()
            #+timedelta(minutes=i)
            #i=i+1
                #hashkey="1234"
                #gender="Male"
                #age="25"
                #temp="98"
                #hr="72"
                #sys="67"
                #dia="90"
                #spo2="100"
                #ci='5'
            PATIENT = "INSERT INTO MEDICAL_INFO (Hashkey,Time,Gender,Age,Temperature,HeartRate,Systole,Diastole,Spo2,CriticalIndex) VALUES (%s,%s,%s, %s, %s,%s,%s,%s,%s,%s)"
            val = (hashkey,time,gender,age,temp,hr,sys,dia,spo2,ci)
            print(val)
            mycursor.execute(PATIENT, val)

            mydb.commit()

    
    return render_template('details.html',name=name)
@app.route("/heartrate")
def heartrate():
    return render_template('heartrate.html')

@app.route("/offlineheartrate")
def offlineheartrate():
    return render_template('offlineheartrate.html')

@app.route('/heartratedata', methods=["GET"])
def heartratedata():
    def generate_heartrate_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y,z= line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_heartrate_data(), mimetype='text/event-stream')
@app.route('/offlineheartratedata', methods=["GET"])
def offlineheartratedata():
    def generate_offlineheartrate_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y,z= line.split(',')
                xs.append(int(x))  
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_offlineheartrate_data(), mimetype='text/event-stream')
@app.route("/temperature")
def temperature():
    return render_template('temperature.html')
@app.route("/offlinetemperature")
def offlinetemperature():
    return render_template('offlinetemperature.html')


@app.route('/temperaturedata', methods=["GET"])
def temperaturedata():
    def generate_temperature_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y,z= line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(z)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_temperature_data(), mimetype='text/event-stream')
@app.route('/offlinetemperaturedata', methods=["GET"])
def offlinetemperaturedata():
    def generate_offlinetemperature_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y,z= line.split(',')
                xs.append(int(x))  
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(z)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)
    return Response(generate_offlinetemperature_data(), mimetype='text/event-stream')
@app.route("/ecg")
def ecg():
    return render_template('ecg.html')
@app.route("/offlineecg")
def offlineecg():
    return render_template('offlineecg.html')

@app.route('/ecgdata', methods=["GET"])
def ecgdata():
    def generate_ecg_data():
        open("ECG.txt", "w").close()
        os.system('python3 grabserial_ECG >> ECG.txt')
        graph_data = open('ECG.txt','r').read()
        lines = graph_data.split('\n')
        for line in lines:  
            if len(line)>=1:
                #x,y,z=line.split(',')
                x=line  
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_ecg_data(), mimetype='text/event-stream')
@app.route('/offlineecgdata', methods=["GET"])
def offlineecgdata():
    def generate_offlineecg_data():
        open("ECG.txt", "w").close()
        os.system('python3 grabserial_ECG >> ECG.txt')
        graph_data = open('ECG.txt','r').read()
        lines = graph_data.split('\n')
        for line in lines:  
            if len(line)>=1:
                #x,y,z=line.split(',')
                x=line  
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)


    return Response(generate_offlineecg_data(), mimetype='text/event-stream')

@app.route("/spo2")
def spo2():
    return render_template('spo2.html')
@app.route("/offlinespo2")
def offlinespo2():
    return render_template('offlinespo2.html')


@app.route('/spo2data', methods=["GET"])
def spo2data():
    def generate_spo2_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y,z = line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(y)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_spo2_data(), mimetype='text/event-stream')
@app.route('/offlinespo2data', methods=["GET"])
def offlinespo2data():
    def generate_offlinespo2_data():
        open("spo2.txt", "w").close()
        os.system('python3 grabserial_spo2_temp >> spo2.txt')
        graph_data = open('spo2.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y,z = line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(y)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_offlinespo2_data(), mimetype='text/event-stream')

@app.route("/bloodpressure")
def bloodpressure():
    return render_template('bloodpressure.html')
@app.route("/offlinebloodpressure")
def offlinebloodpressure():
    return render_template('offlinebloodpressure.html')


@app.route('/bloodpressuredata', methods=["GET"])
def bloodpressuredata():
    def generate_bloodpressure_data():
        open("BP.txt", "w").close()
        os.system('python3 grabserial_BP >> BP.txt')
        graph_data = open('BP.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y= line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(y)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_bloodpressure_data(), mimetype='text/event-stream')
@app.route('/offlinebloodpressuredata', methods=["GET"])
def offlinebloodpressuredata():
    def generate_offlinebloodpressure_data():
        open("BP.txt", "w").close()
        os.system('python3 grabserial_BP >> BP.txt')
        graph_data = open('BP.txt','r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []
        for line in lines:   
            if len(line) > 1:
                x, y= line.split(',')
                xs.append(int(x))
                ys.append(int(y))
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': int(y)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_offlinebloodpressure_data(), mimetype='text/event-stream')


@app.route("/criticalindex")
def criticalindex():
    return render_template('criticalindex.html')

@app.route("/offlinecriticalindex")
def offlinecriticalindex():
    return render_template('offlinecrticalindex.html')

@app.route('/criticalindexdata', methods=["GET"])
def criticalindexdata():
    def generate_criticalindex_data():
        #open("PERSONAL_INFO.txt", "w").close()
        open("CI.txt", "w").close()
        os.system("python3 ml2.py >> CI.txt")
        graph_data = open('CI.txt','r').read()
        lines = graph_data.split('\n')
        for line in lines:
            if len(line)>=1:
                #x,y,z=line.split(',')
                x=line
                print(x)
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)

    return Response(generate_criticalindex_data(), mimetype='text/event-stream')
@app.route('/offlinecriticalindexdata', methods=["GET"])
def offlinecriticalindexdata():
    def generate_offlinecrticalindex_data():
        #open("PERSONAL_INFO.txt", "w").close()
        #os.system('python3 grabserial_F_ENROLL >> FP.txt')
        open("CI.txt", "w").close()
        os.system("python3 ml2.py >> CI.txt") 
        graph_data = open('CI.txt','r').read()
        lines = graph_data.split('\n')
        for line in lines:  
            if len(line)>=1:
                #x,y,z=line.split(',')
                x=line  
                print(x)
        #while True:
                json_data = json.dumps(
                    {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': float(x)})
                yield f"data:{json_data}\n\n"
                time.sleep(1)



    return Response(generate_offlinecrticalindex_data(), mimetype='text/event-stream')

@app.route("/fingerprintenroll")
def fingerprintenroll():
    open("F_ENROLL.txt", "w").close()
    os.system('python3 grabserial_F_ENROLL -e 10 >> F_ENROLL.txt')
    return render_template("enroll_state.html")
    #def fingerprintenrolldata():
        #os.system('python3 grabserial_F_ENROLL >> FP.txt')
        #graph_data = open('FP.txt','r').read()
        #lines = graph_data.split('\n')
        #for line in lines:
            #if len(line) > 1:
                #x= line
        #filepath = 'FP.txt'
        #with open(filepath) as fp:
            #line = fp.readline()
            #while line:
                #line = fp.readline()
         
              
        #while True:
                #json_data = json.dumps({'value':x})
                #yield f"data:{json_data}\n\n"
                #time.sleep(5)

    #return Response(fingerprintenrolldata(), mimetype='text/event-stream')
@app.route("/offlineadministrator",methods=["GET", "POST"])
def offlineadministratorlogin():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        if(uname=='EpioneNG' and passw=='0000'):
            return render_template('offlineadministratordetails.html')
    return render_template('offlineadministrator.html')
@app.route("/administratorlogin",methods=["GET","POST"])
def administrator():
    if request.method == "POST":
        uname = request.form["uname"]
        passw = request.form["passw"]
        if(uname=='EpioneNG' and passw=='0000'):
            return render_template('administratordetails.html')
    return render_template('administrator.html')
@app.route("/getip",methods=["GET","POST"])
def getip():
    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)
    return ({"ip":IPAddr},{"Host":hostname})

@app.route("/stop")
def stop():
    os._exit(0)
    return 'Fingerprint Enrolled Successfully'
@app.route("/enroll_state")
def enroll_state():
    return render_template("enroll_state.html") 
@app.route("/loginviafingerprint",methods=["GET","POST"])
def loginviafingerprint():

    open("F_LOGIN.txt", "w").close()
    os.system('python3 grabserial_F_LOGIN -e 10 >> F_LOGIN.txt')
    return render_template("login_state.html")
@app.route("/fingerdetails",methods=["GET","POST"])
def fingerdetails():
    #time.sleep(30)
    #os.system("pgrep -f grabserial_F_LOGIN")
    #os.system("pkill -9 -f grabserial_F_LOGIN")
    graph_data = open('F_LOGIN.txt','r').read()
    lines = graph_data.split('\n')
    for line in lines:
        if len(line) >= 1:
        #x,y=line.split(',')
            x=line
  
    #mail="sa@gmail.com"
    #passw="1234"
    mydb = mysql.connector.connect(
    host="10.14.79.58",
    user="root",
    passwd="12345",
    database="PATIENT")
    #print(type(mail))
    #print(mail)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM PATIENT_INFO WHERE Fingerprint = %s"%x)
    # Fetch one record and return result
    account = mycursor.fetchone()
    print(account)
    mydb.commit()
    if account:
        mydb = mysql.connector.connect(
        host="10.14.79.58",
        user="root",
        passwd="12345",
        database="PATIENT")

        mycursor = mydb.cursor()
        mycursor.execute("SELECT Name FROM PATIENT_INFO WHERE Fingerprint = %s"%x)
        # Fetch one record and return result
        name = str(mycursor.fetchone()[0])
        mydb.commit()

        return render_template("details.html",name=name)
    return render_template("login_state.html")
@app.route("/login_state")
def login_state():
    return render_template("login_state.html")


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
