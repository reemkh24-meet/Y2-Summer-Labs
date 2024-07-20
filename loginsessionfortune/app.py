from flask import Flask, render_template, request, redirect, url_for
from flask import session as login_session

app = Flask(__name__)
app.secret_key = 'PASSWORD'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        birth_month = request.form['birth_month']
        login_session['username'] = username
        login_session['birth_month'] = birth_month
        return redirect(url_for('home', user=username))

@app.route('/home')
def home():
    user = login_session.get('username')
    return render_template('home.html', user=user)

@app.route('/fortune')
def fortune():
    month= login_session.get('birth_month')
    fortune_list = [
        "A lifetime of happiness lies ahead of you!",
        "A beautiful, smart, and loving person will be coming into your life.",
        "A dubious friend may be an enemy in camouflage.",
        "A faithful friend is a strong defense.",
        "A fresh start will put you on your way.",
        "A friend asks only for your time not your money.",
        "A friend is a present you give yourself.",
        "A golden egg of opportunity falls into your lap this month.",
        "A lifetime friend shall soon be made."
    ]
    index = len(month) 
    if 1 <= index <= 9:
        return render_template("fortune.html", f=fortune_list[index-1])
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

