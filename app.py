from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def index():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/services')
def services():
    if request.method == 'GET':
        return render_template('services.html')


@app.route('/about')
def about():
    if request.method == 'GET':
        return render_template('about.html')


@app.route('/appointments')
def appointments():
    if request.method == 'GET':
        return render_template('appointments.html')


if __name__ == '__main__':
    app.run()
