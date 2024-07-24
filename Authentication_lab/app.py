from flask import Flask, render_template,url_for,redirect,request, session 
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAUiR-mC2rhoczvAKefYfS0tzHHXbu8Gag",
    "authDomain": "reem-meet2025.firebaseapp.com",
    "projectId": "reem-meet2025",
    "storageBucket": "reem-meet2025.appspot.com",
    "messagingSenderId": "466005672092",
    "appId": "1:466005672092:web:280c43af818398d09ded59",
    "measurementId": "G-7CBEZG9DLN",
    "databaseURL": "https://reem-meet2025-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = "PASSWORD"

@app.route('/', methods = ['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        full_name = request.form['full_name']
        try:
            user = {'email' : email, 'username': username, 'full_name': full_name}
            session['user'] = auth.create_user_with_email_and_password(email, password)
            db.child('Users').child(session['user']['localId']).set(user)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return redirect(url_for("error"))
    return render_template("signup.html")


@app.route('/sign-in', methods=['GET','POST'])
def signIn():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            error = "Authentication failed"
            return redirect(url_for("error"))
    return render_template("signin.html")


@app.route('/home', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        quote = request.form['quote']
        speaker = request.form['speaker']
        session['speaker'] = speaker
        session['quote'] = quote
        quote_info= {'said_by' : speaker,'quote': quote, 'uid' : session['user']['localId']}
        db.child('Quotes').push(quote_info)
        return redirect(url_for('thanks'))
    return render_template('home.html')



@app.route('/display')
def display():
    return render_template("display.html")




@app.route('/thanks')
def thanks():
    if session['user'] != None:
        quote = session['quote']
        speaker = session['speaker']
        return render_template("thanks.html",quote = quote, speaker = speaker)
    else:
        return redirect(url_for('signIn'))



@app.route('/sign-out')
def signOut():
    session['user']=None
    auth.current_user = None
    return redirect(url_for('signIn'))



@app.route('/error.html')
def error():
    return render_template('error.html')
if __name__ == '__main__':
    app.run(debug=True)