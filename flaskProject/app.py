from flask import Flask, render_template, session, request, flash, redirect

app = Flask(__name__)
app.secret_key = "abchhsdsgfhsd"

@app.route('/')
def register():
    return render_template("register.html")

@app.route('/loadlogin')
def loadlogin():
    return render_template("login.html")

@app.route('/registration', methods=['post'])
def registration():
    fn = request.form.get("fn")
    ln = request.form.get("ln")
    un = request.form.get("un")
    password = request.form.get("password")
    session['k1'] = fn
    session['k2'] = ln
    session['k3'] = un
    session['k4'] = password
    return render_template('login.html')

@app.route('/login', methods=['post'])
def login():
    un = request.form.get("un")
    password = request.form.get("password")

    if session['k3'] == un and session['k4'] == password:
        data = session['k1'] + " " + session['k2']
        return render_template('welcome.html', data=data)
    else:
        flash("user name and password does not match")
        return redirect('/loadlogin')


if __name__ == "__main__":
    app.run(threaded=True, debug=True, host="localhost", port=5000)

