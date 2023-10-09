from flask import Flask, render_template


app = Flask("scissorsBeautySalon")


@app.route('/')
def home():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/')
def Services():
    if request.method == 'GET':
        return render_template('services.html')


@app.route('/')
def About():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
