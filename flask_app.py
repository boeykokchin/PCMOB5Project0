
# A very simple Flask Hello World app for you to get started with...
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcbmi')
def calcbmi():
    weight = float(request.args["weight"])
    height = float(request.args["height"])
    name = request.args["name"]
    bmi = weight / (height ** 2)
    return name + "'s BMI is " + str(bmi)


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
