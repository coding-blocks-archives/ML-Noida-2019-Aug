from flask import Flask, render_template, request, redirect

import pred

app = Flask("My-App")

@app.route("/", methods=["get"])
def hello():
    return render_template("form.template", result = "")

@app.route("/submit", methods=["post"])
def submit_form():
    result = pred.predict(request.form["text"])
    return render_template("form.template", result = result)

@app.route("/submit", methods=["get"])
def submit_redirect():
    return redirect("/")