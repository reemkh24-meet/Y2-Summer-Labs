from flask import Flask, render_template, request, redirect, url_for, session
import pyrebase

firebaseConfig = {
  "apiKey": "AIzaSyBrb4HFd__DMFWZyNS833Pe2Tdru17hGAY",
  "authDomain": "firstproject-meet.firebaseapp.com",
  "databaseURL": "https://firstproject-meet-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "firstproject-meet",
  "storageBucket": "firstproject-meet.appspot.com",
  "messagingSenderId": "248879289870",
  "appId": "1:248879289870:web:9a1fb8021ba47f7a524e5f",
  "measurementId": "G-7SWPS9TNSX",
  "databaseURL": "https://firstproject-meet-default-rtdb.europe-west1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = "PASSWORD"

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method=="POST":

    # if request.method == 'POST':
         email = request.form['email']
         password = request.form['password']
    #     username = request.form['username']

         try:
             user=auth.sign_in_user_with_email_and_password(email, password)
             session["user"]=user
             return redirect(url_for('home'))
    #         db.child('Users').child(auth.current_user['localId']).set(user)
    #         return redirect(url_for('home'))
         except Exception as e:
             error = "Authentication failed"
             print(e)
             return render_template("signupin.html", error=error)

    else:
        return render_template("signupin.html")

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        score=0
        email = request.form['email']
        password = request.form['password']
        username = request.form['username']
        try:
            user = auth.create_user_with_email_and_password(email, password)
            session["user"]=user
            user_data = {
                'username': username,
                'email': email,
                'password':password,
                'score':score
            }
            db.child('Users').child(session['user']['localId']).set(user_data)
            return redirect(url_for('home'))

        except Exception as e:
            error = "Authentication failed"
            print(e)
            return render_template("signup.html", error=error)

    return render_template("signup.html")

@app.route('/action_page.php', methods=['GET','POST'])
def show_contact_form():
    return render_template('thank_you.html')

@app.route('/home',methods=['GET', 'POST'])
def home():
    if 'user' in session:
        return render_template("home.html")
    else:
        return redirect(url_for('signin'))

@app.route('/result',methods=['GET', 'POST'])
def result():
    score=db.child('Users').child(session['user']['localId']).child("score").get().val()
    return render_template("result.html",score=score)
    
@app.route('/easy', methods=['GET', 'POST'])
def easy():
    if request.method == "POST":
        # Get all form data into a dictionary
        form_data = request.form.to_dict()

        user_id = session['user']['localId']
        user = db.child('Users').child(user_id).get().val()

        score = 0

        # Loop through each question and check answers
        for i in range(1, 16):
            question_key = f"answer_{i}"
            correct_answer_key = f"correct_answer_{i}"

            user_answer = form_data.get(question_key, "").strip()
            correct_answer = form_data.get(correct_answer_key, "").strip()

            # Compare user's answer with correct answer
            if user_answer.lower() == correct_answer.lower():
                score += 1

        # Update the score in the database
        db.child('Users').child(user_id).update({'score': score})

        return redirect(url_for("result"))

    return render_template("easy.html")




@app.route('/mid', methods=['GET', 'POST'])
def mid():
    if request.method == "POST":
        # Get all form data into a dictionary
        form_data = request.form.to_dict()

        user_id = session['user']['localId']
        user = db.child('Users').child(user_id).get().val()

        score = 0

        # Loop through each question and check answers
        for i in range(1, 16):
            question_key = f"answer_{i}"
            correct_answer_key = f"correct_answer_{i}"

            user_answer = form_data.get(question_key, "").strip()
            correct_answer = form_data.get(correct_answer_key, "").strip()

            if user_answer.lower() == correct_answer.lower():
                score += 1

        # Update the score in the database
        db.child('Users').child(user_id).update({'score': score})

        return redirect(url_for("result"))

    return render_template("mid.html")

@app.route('/hard', methods=['GET', 'POST'])
def hard():
    if request.method == "POST":
        # Get all form data into a dictionary
        form_data = request.form.to_dict()

        user_id = session['user']['localId']
        user = db.child('Users').child(user_id).get().val()

        score = 0

        # Loop through each question and check answers
        for i in range(1, 16):
            question_key = f"answer_{i}"
            correct_answer_key = f"correct_answer_{i}"

            user_answer = form_data.get(question_key, "").strip()
            correct_answer = form_data.get(correct_answer_key, "").strip()

            # Compare user's answer with correct answer
            if user_answer.lower() == correct_answer.lower():
                score += 1

        # Update the score in the database
        db.child('Users').child(user_id).update({'score': score})

        return redirect(url_for("result"))

    return render_template("hard.html")

@app.route('/sign-out')
def signOut():
    session['user']=None
    auth.current_user = None
    return redirect(url_for('signup'))
if __name__ == '__main__':
    app.run(debug=True)
