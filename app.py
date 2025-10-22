from flask import Flask, request, redirect, url_for, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['pwd']

    if not username:
        return "<script>alert('Username cannot be empty.'); window.history.back();</script>"
    elif not password:
        return "<script>alert('Password cannot be empty.'); window.history.back();</script>"
    elif len(password) < 6:
        return "<script>alert('Password must be at least 6 characters long.'); window.history.back();</script>"
    else:
        return redirect('/result')   # ✅ redirect to result page instead of /submit

@app.route('/result')
def result():
    return render_template('greeting.html')
