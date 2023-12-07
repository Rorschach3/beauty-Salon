from datetime import timedelta

from flask import Flask, flash, redirect, render_template, request, session


app = Flask(__name__)
app.secret_key = "secret key"
app.permanent_session_lifetime = timedelta(hours=24)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/services', methods=["POST", "GET"])
def services():
    if request.method == 'GET':
        return render_template('services.html')


@app.route('/about', methods=["POST", "GET"])
def about():
    if request.method == 'GET':
        return render_template('about.html')


@app.route('/appointments', methods=["POST", "GET"])
def appointments():
    if request.method == 'GET':
        session.permanent = True
        # appt = request.form.get("appt")
        # session["appt"] = appt
        return render_template('appointments.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
