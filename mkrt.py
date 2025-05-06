from flask import Flask, redirect, render_template, request, url_for
import mysql.connector



app = Flask(__name__)

def get_db_connection():
        connection = mysql.connector.connect(
        host='localhost',  # Adresa serverului MySQL
        user='root',  # Numele utilizatorului MySQL
        password='rarescst',  # Parola pentru utilizator
        database='mkrt'  # Numele bazei de date
        )

        return connection

@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/get-started")
def get_started():
    return render_template("get-started.html")

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/servicii_web_design", methods =['get', 'post'])
def servicii_web_design():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Conectare la baza de date și inserare a datelor
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, phone_nmb, email) VALUES (%s, %s, %s)", (name, phone, email))
        conn.commit()  # Salvarea modificărilor
        cursor.close()
        conn.close()

        # return redirect(url_for('home'))  # Redirect după trimiterea datelor

    return render_template("servicii_web_design.html")

@app.route("/google_ads", methods =['get', 'post'])
def google_ads():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Conectare la baza de date și inserare a datelor
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, phone_nmb, email) VALUES (%s, %s, %s)", (name, phone, email))
        conn.commit()  # Salvarea modificărilor
        cursor.close()
        conn.close()
    
    return render_template("google_ads.html")

@app.route("/comunicare_scm", methods =['get', 'post'])
def comunicare_scm():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        # Conectare la baza de date și inserare a datelor
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO clients (name, phone_nmb, email) VALUES (%s, %s, %s)", (name, phone, email))
        conn.commit()  # Salvarea modificărilor
        cursor.close()
        conn.close()
    return render_template("comunicare_scm.html")

@app.route("/tiktok_ads")
def tiktok_ads():

    return render_template("tiktok_ads.html")


if __name__ == '__main__':
   
    app.run(debug=True, port=8000)
