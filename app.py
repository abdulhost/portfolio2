from flask import Flask, render_template , request,flash
from flask_mysqldb import MySQL
import time

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] ='mysql://id20990148_portfolio:Webhost@159@localhostid20990148_portfolio'
app.secret_key = '159'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'id20990148_portfolio'
app.config['MYSQL_PASSWORD'] = 'Webhost@159'
app.config['MYSQL_DB'] = 'id20990148_portfolio'
mysql = MySQL(app)

# @app.route('/')
# def hello_world():
#     return render_template('index.html')

# class data(db.Model):
#     name = db.Column(db.String(20), nullable=False ,primary_key=True)
#     email = db.Column(db.String(80),nullable=False )
#     msg = db.Column(db.String(120), nullable=False )




@app.route("/", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('msg')

        # entry = data(name=name, email = email, msg = message)

        cur = mysql.connection.cursor()

        cur.execute("INSERT INTO data VALUES (%s,%s,%s)",(name,email,msg))

        # db.session.add(entry)
        mysql.connection.commit()
        cur.close()
        loggedin=True
        flash('Your Message was Delivered Successfully', 'success')
        return render_template('index.html')
        
   
    return render_template('index.html')

@app.route("/login" ,methods = ['GET', 'POST'])
def show():
    if(request.method=='POST'):
        
        email = request.form.get('email')
        password = int(request.form.get('pass') )
        cur=mysql.connection.cursor()
        cur.execute('SELECT * FROM admin')
        acc=cur.fetchall()
        
        for u in acc:
            row=u[0]
            row2=u[1]
            
        print(row)
        print(row2)

        
        if email == row and password == row2:
            print("login success")
            users=cur.execute("SELECT * FROM data")
            ud= cur.fetchall()
            return render_template('alldata.html',ud=ud) 
            
        else:
            print("access denied")

        


    return render_template('alldata.html')


if __name__=="__main__":
    app.run(debug=True)
