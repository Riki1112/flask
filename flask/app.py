from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Simulasi database sementara
users = {"user@gmail.com": "123"}
user_role = "kurir"
total_belanja = 120000

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    if email in users and users[email] == password:
        return redirect(url_for('menu'))
    else:
        return "Login gagal. <a href='/'>Coba lagi</a>"

@app.route('/menu')
def menu():
    now = datetime.now()
    jam = now.hour
    if jam > 21:
        return render_template('tutup.html')
    return render_template('menu.html')

@app.route('/kurir')
def kurir():
    if user_role == "kurir":
        return render_template('kurir.html')
    else:
        return "Bukan halaman untukmu."

@app.route('/checkout')
def checkout():
    return render_template('checkout.html', total=total_belanja)

@app.route('/alamat', methods=['GET', 'POST'])
def alamat():
    if request.method == 'POST':
        alamat = request.form['alamat']
        if alamat.strip() == "":
            return render_template('alamat.html', error="Alamat tidak boleh kosong")
        return "Alamat berhasil disimpan!"
    return render_template('alamat.html', error="")

if __name__ == '__main__':
    app.run(debug=True)
