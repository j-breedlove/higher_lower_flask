import random

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
rand_number = random.randint(0, 9)


@app.route('/', methods=['GET', 'POST'])
def pick_a_number():
    """Route to prompt the user to guess a number.
    If the form is submitted, redirect to the guess_number route."""
    if request.method == 'POST':
        user_guess = request.form.get('guess')
        return redirect(url_for('guess_number', number=user_guess))
    return render_template('index.html')


@app.route('/guess/<int:number>')
def guess_number(number):
    """Route to display the result of the user's guess."""
    if number > rand_number:
        return render_template('result.html', outcome='high')
    elif number < rand_number:
        return render_template('result.html', outcome='low')
    else:
        return render_template('result.html', outcome='correct')


if __name__ == '__main__':
    app.run()
