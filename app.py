from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'stonepaperscissors'

choices = ['stone', 'paper', 'scissors']

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'ucount' not in session:
        session['ucount'] = 0
        session['ccount'] = 0

    result = ""
    user_choice = ""
    comp_choice = ""

    if request.method == 'POST':
        user_choice = request.form['choice']
        comp_choice = random.choice(choices)

        if user_choice == comp_choice:
            result = "It's a Draw!"
        elif (user_choice == 'stone' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'stone') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            session['ucount'] += 1
            result = "You Win!"
        else:
            session['ccount'] += 1
            result = "Computer Wins!"

    return render_template("index.html",
                           ucount=session['ucount'],
                           ccount=session['ccount'],
                           result=result,
                           user_choice=user_choice,
                           comp_choice=comp_choice)

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
