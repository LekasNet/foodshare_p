from flask import Flask, render_template, url_for, request, flash, redirect
from jinja2 import Environment, FileSystemLoader, select_autoescape
from flask_ngrok import run_with_ngrok
from forms import LoginForm
import os


app = Flask(__name__, static_folder="static")
run_with_ngrok(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

request_name = ''
logins = ['adm', 'adm2', 'adm3']
adm = (request_name in logins)


@app.route('/')
def welcome():
    print(request_name + ' lol ')
    adm = request_name in logins
    return render_template("main_page.html", main="current", adm=adm)


@app.route('/order')
def order():
    ask = render_template('card.html')
    test_page = []
    prev = ''
    for i in range(10):
        num = i // (10 // 2) + 1
        test_page.append(ask.format(str(num)))
    return render_template("order_page.html", order="current", adm=adm).format(' '.join(test_page))


@app.route('/contacts')
def contacts():
    return render_template("contact_page.html", contacts="current", adm=adm)


@app.route('/FAQ')
def faq():
    return render_template("faq_page.html", faq="current", adm=adm)


@app.route('/test')
def test():
    return render_template("test_page.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    global request_name
    form = LoginForm()
    if form.validate_on_submit():
        print('Login requested for user {} with password {}'.format(
            form.username.data, form.password.data))
        request_name = form.username.data
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
    '''port = int(os.environ.get("PORT", 5000))
    host='0.0.0.0', port=port'''
    app.run()
