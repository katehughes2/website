from flask import Flask, render_template, request

app = Flask ("MyApp")

@app.route("/")
def hello():
    return render_template("Googal.html")

@app.route ("/one")
def uncover():
    return render_template("googals_tech.html")

@app.route("/two")
def uncover():
    return render_template("techtrue.html")

@app.route("/end")
def hello():
    return render_template("form.html")

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print form_data["email"]
    return "ALL OK"

app.run(debug=True)
