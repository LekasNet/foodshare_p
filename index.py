from flask import Flask, render_template, url_for, request, flash, redirect
from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask import render_template
from forms import LoginForm
import os


app = Flask(__name__, static_folder="static")
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def welcome():
    return render_template("main_page.html")


@app.route('/order')
def order():
    return render_template("order_page.html")


@app.route('/contacts')
def contacts():
    return render_template("contact_page.html")


@app.route('/FAQ')
def faq():
    return render_template("faq_page.html")


@app.route('/test')
def test():
    return rendered_page


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')