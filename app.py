from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('myForm.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('pwd')

    # Server-side validation (in case JS is bypassed)
    if not username:
        return "<script>alert('Username cannot be empty'); window.history.back();</script>"
    if not password:
        return "<script>alert('Password cannot be empty'); window.history.back();</script>"
    if len(password) < 6:
        return "<script>alert('Password must be at least 6 characters long'); window.history.back();</script>"

    # Valid input → go to greeting page
    return render_template('greeting.html', name=username)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
