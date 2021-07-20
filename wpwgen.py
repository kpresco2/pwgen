from flask import Flask, render_template, url_for,flash, redirect, request, g
from forms import GetArgs
from datetime import date, datetime
import random
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env


app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)

from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField, SelectField, PasswordField, IntegerField
from wtforms.validators import DataRequired, EqualTo, NumberRange, InputRequired
VERSION = '1.00'

def gen_passwords(pass_cnt, digit_cnt, symbol_cnt, upper_cnt, lower_cnt):

    password_list = []
    digit ="1234567890"
    symbol="!@#$%_-=?+[]{}()"
    uppercase="ABCDEFGHIJKLMNOPQRSTUVWZYZ"
    lowercase="abcdefghijklmnopqrstuvwxyz"

    for i in range(1,pass_cnt+1):
        add_ons = []
        #Digits
        for i in range(0,digit_cnt):
            add_ons.append(digit[random.randint(0,len(digit)-1)])
        # Symbols
        for i in range(0,symbol_cnt):
            add_ons.append(symbol[random.randint(0,len(symbol)-1)])
        # Uppercase
        for i in range(0,upper_cnt):
            add_ons.append(uppercase[random.randint(0,len(uppercase)-1)])
        # Uppercase
        for i in range(0,lower_cnt):
            add_ons.append(lowercase[random.randint(0,len(lowercase)-1)])

        # Shuffle the Add Ons
        random.shuffle(add_ons)
        # random.shuffle(add_ons)
        # random.shuffle(add_ons)

        password = ""
        for i in add_ons:
            password += i

        password_list.append(password)
        print(password)

    return password_list


@app.route("/", methods=['GET','POST'])
def pwgen():
    form = GetArgs()
    pwords = []
    if request.method == "POST":
        if form.validate_on_submit():
            pwords = gen_passwords(int(request.form['pass_cnt']), int(request.form['digit_cnt']),
                int(request.form['symbol_cnt']), int(request.form['upper_cnt']), int(request.form['lower_cnt']))
            form.hpwords.data = pwords
            return render_template('index.html', pwords=pwords, form=form)
        else:
            pwords = eval(request.form['hpwords'])
            return render_template('index.html', pwords=pwords, form=form)
    else:
        pwords = gen_passwords(5, 2, 1, 4, 9)
        form.hpwords.data = pwords
        return render_template('index.html', pwords=pwords, form=form)

@app.route("/about")
def about():
    return render_template('about.html', version=VERSION)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
