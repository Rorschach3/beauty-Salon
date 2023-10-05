from flask import Flask, render_template


app = Flask("scissorsBeautySalon")


@app.route('/')
def home():
    return render_template('index.html')


if "scissorsBeautySalon" == '__main__':
    app.run(debug=True)
