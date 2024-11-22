from flask import Flask, render_template,request, redirect
import sqlite3
from twilio.rest import Client
import random
app = Flask(__name__)


ACCOUNT_SID = 'AC835b5e3669038ca50a97fd1265bf823c'
AUTH_TOKEN = '1e42eb7c187dbb938866251d0fa378e6'
TWILIO_PHONE = '+12029725129'

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def create_connection():
    conn = sqlite3.connect("Contact.db")
    return conn

def create_table():
    conn = create_connection()
    cur =conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS newcontact(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, number TEXT)')
    conn.commit()
    conn.close()

@app.route('/admin')
def admin():
    conn = create_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM newcontact')
    data = cur.fetchall()
    return render_template('admin.html', users=data)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method == 'POST':
        name= request.form['inp1']
        num= request.form['inp2']
        conn = create_connection()
        cur= conn.cursor()
        cur.execute('''INSERT INTO newcontact(name,number) VALUES(?,?)''',(name,num))
        conn.commit()
        conn.close()
        admin(


        )
    return render_template("contact.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

def send_otp():
  
    phone_number = "+919381666049"
    
    otp = random.randint(100000, 999999)

        # Send OTP via Twilio
    message = client.messages.create(body=f"Your OTP is: {otp}",from_=TWILIO_PHONE,to=phone_number)



if __name__ == "__main__":
    create_connection()
    create_table()
    send_otp()
    app.run(debug=True)