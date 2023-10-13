from flask import Flask, render_template, request, send_from_directory
import os


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


@app.route('/images/facebook.png')
def get_image():
    image_directory = os.path.join(app.root_path, 'images')
    filename = 'facebook.png'
    return send_from_directory(image_directory, filename)


if __name__ == '__main__':
    app.run()
