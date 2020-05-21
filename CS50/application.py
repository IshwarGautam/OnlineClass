from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
    #name=request.args.get("name","world") #if not provide name, world is default value
    #return render_template("index.html",name=name)
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    if not request.form.get("name") or not request.form.get("Field"):
        return render_template("failure.html")
    with open("registered.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((request.form.get("name"), request.form.get("Field")))
    return render_template("success.html")


@app.route("/registered")
def registered():
    with open("registered.csv", "r") as file:
        reader = csv.reader(file)
        students = list(reader)
        students=filter(None, students)
        print(students)
    return render_template("registered.html", students=students)

app.run(debug=True)