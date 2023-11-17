from flask import Flask, render_template, request, redirect, url_for
import csv
from flask_cors import CORS

app = Flask(__name__, template_folder='template', static_folder='static')
CORS(app)

@app.route("/")
def main():
    return render_template('main.html')

@app.route('/biodata/')
def biodata():
    return render_template('Biodata.html')

@app.route('/cv/')
def cv():
    return render_template('CV.html')

@app.route("/portfolio/")
def portfolio():
    return render_template('portfolio.html')

@app.route('/mygalery/')
def mygalery():
    return render_template('mygalery.html')


@app.route("/fibonacci/", methods=['GET', 'POST'])
def fibonacci():
    if request.method == 'POST':
        n = int(request.form['number'])
        fibo = [1, 1]
        for i in range(n-1):
            fibo.append(fibo[i] + fibo[i+1])
        result = fibo
        return render_template('fibo.html', number=n, result=result)
    return render_template('fibo.html')


@app.route('/csv2json/', methods=['GET'])
def csv2json():
    csv_file_path = 'static/data.csv'
    data = []

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for i in csv_reader:
            data.append(i)
    return render_template("csv2json.html", json_data=data)

@app.route("/form/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        return redirect(url_for("resultform", name=name, age=age))
    return render_template("form.html")

@app.route("/resultform/")
def resultform():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("resultform.html", name=name, age=age)
