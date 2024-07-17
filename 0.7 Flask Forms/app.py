from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        birth_month = request.form['birthmonth']
        return redirect(url_for('fortune', month=birth_month))

@app.route('/fortune/<month>')
def fortune(month):
    fortune_list=["A lifetime of happiness lies ahead of you.","A beautiful, smart, and loving person will be coming into your life.","A dubious friend may be an enemy in camouflage.","A faithful friend is a strong defense.","A fresh start will put you on your way.","A friend asks only for your time not your money.","A friend is a present you give yourself.","A golden egg of opportunity falls into your lap this month.","A lifetime friend shall soon be made."]
    index=len(month)
    if index>0 and index<=9:
        return render_template("fortune.html",f=fortune_list[index-1])
    else:
        return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True, port = 5001)