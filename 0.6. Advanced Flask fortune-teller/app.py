from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('hello.html')

@app.route('/fortune')
def fortune():
    fortune_list=["A light heart carries you through all the hard times.","A lifetime of happiness lies ahead of you.","A beautiful, smart, and loving person will be coming into your life.","A dubious friend may be an enemy in camouflage.","A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A friend is a present you give yourself.","A golden egg of opportunity falls into your lap this month.","A lifetime friend shall soon be made."]
    random_fortune=fortune_list[random.randint(0,10)]
    return render_template("fortune.html",f=random_fortune)

if __name__ == '__main__':
    app.run(debug=True, port = 5001)