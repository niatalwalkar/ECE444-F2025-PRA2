#example 2-1
# from flask import Flask 
# app = Flask(__name__) 
# @app.route('/') 
# def index(): 
#     return '<h1>Hello World!</h1>'

#example 2-2
# from flask import Flask
# app = Flask(__name__) 
# @app.route('/') 
# def index(): 
#     return '<h1>Hello World!</h1>'

# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'ECE444 PRA2 Activity 1.4'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators = [DataRequired()])
    email = StringField('UofT email', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/user/<name>')
# def user(name):
#     return render_template('user.html', name = name)

@app.route('/', methods = ['GET', 'POST'])
def base():
    # name = None
    form = NameForm()
    if form.validate_on_submit():
        # name = form.name.data
        old_name = session.get('name')
        # form.name.data = ''
        if 'utoronto' in form.email.data.lower():
            session['name'] = form.name
            session['email']= form.email
        else:
            flash('Please enter a UofT email address')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        return redirect(url_for('base'))
    # return render_template("index.html", name = "Nia", form = form, current_time = datetime.utcnow())
    return render_template("index.html", name=session.get('name', None), email=session.get('email'),form = form, current_time = datetime.utcnow())
#  current_time = datetime.utcnow()