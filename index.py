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
    ask = render_template('card.html')
    test_page = [ask for _ in range(10)]
    return render_template("order_page.html").format(' '.join(test_page))


@app.route('/contacts')
def contacts():
    return render_template("contact_page.html")


@app.route('/FAQ')
def faq():
    return render_template("faq_page.html")


@app.route('/test')
def test():
    return render_template("test_page.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('Login requested for user {} with password {}'.format(
            form.username.data, form.password.data))
        return redirect('/')
    return render_template('login.html', title='Sign In', form=form)


"""
@app.route('/add_card', methods=['GET', 'POST'])
def add_card():
    form = LoginForm()
    if form.validate_on_submit():
        f = form.photo.data
        datafilename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)
"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
