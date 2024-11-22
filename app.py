from flask import Flask, render_template,request, redirect
import sqlite3
import random
app = Flask(__name__)


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



if __name__ == "__main__":
    create_connection()
    create_table()
    send_otp()
    app.run(debug=True)
