from flask import Flask,render_template,request
import pymysql

app=Flask(__name__,template_folder='template')

@app.route("/",methods=["GET","POST"])
    
def register():
    if request.method=="POST":
        
        email= request.form.get('Email')
        password= request.form.get('password')
    
        connection =pymysql.connect(host="localhost", user="root", passwd="", database="king")
        cursor = connection.cursor() 

        cursor.execute("select * from register where email=(%s)",(email))
        data=cursor.fetchone()
        if data is  None:

            

            cursor.execute("INSERT INTO register VALUES (%s, %s)",(email,password))
            connection.commit()
            connection.close()
            return render_template("index2.html")
        else:
            return render_template("index3.html") 
          
  
    return render_template("index.html")
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        
        email= request.form.get('Email')
        password= request.form.get('password')
        connection =pymysql.connect(host="localhost", user="root", passwd="", database="king")
        cursor = connection.cursor() 

        cursor.execute("select * from register where email=(%s) and password=(%s)",(email,password))
        data=cursor.fetchone()
        if data is not None:

            connection.close()
            return render_template("index5.html")
        else:
            return render_template("index6.html") 
          
  
    
    return render_template("login.html")

     
app.run(debug=True)  
