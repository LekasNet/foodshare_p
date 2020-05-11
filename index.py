from flask import Flask, render_template, url_for, request, flash, redirect
from jinja2 import Environment, FileSystemLoader, select_autoescape
from werkzeug.utils import secure_filename
from flask_ngrok import run_with_ngrok
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Foodshare, Base
from forms import LoginForm
from random import randint
import os

engine = create_engine('sqlite:///FoodShare.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__, static_folder="static")
debug = 1
if not debug:
    run_with_ngrok(app)


SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


request_name = ''
logins = ['adm', 'adm2', 'adm3']
adm = (request_name in logins)


def naming():
    while True:
        image_request = randint(0, 100000000)
        try:
            open(f"static/img/{image_request}.jpg")
        except FileNotFoundError:
            return image_request


@app.route('/')
def welcome():
    print(request_name + ' lol ')
    adm = request_name in logins
    return render_template("main_page.html", main="current", adm=adm)


@app.route('/order')
def order():
    test_page = []
    for i in session.query(Foodshare).filter_by(confirmed=1).all():
        image = f"static/img/{i.image}.jpg"
        test_page.append(render_template("card.html", name=i.name, price=i.price, description=i.description, image=image))
        session.commit()
    adm = request_name in logins
    return render_template("order_page.html", order="current", adm=adm).format(' '.join(test_page))


@app.route('/contacts')
def contacts():
    adm = request_name in logins
    return render_template("contact_page.html", contacts="current", adm=adm)


@app.route('/FAQ')
def faq():
    adm = request_name in logins
    return render_template("faq_page.html", faq="current", adm=adm)


@app.route('/test')
def test():
    return render_template("test_page.html")


@app.route("/contribute", methods=['GET', 'POST'])
def give_page():
    if request.method == "GET":
        return render_template('contribute.html')
    elif request.method == 'POST':
        image = naming()
        email = request.form['email']
        password = request.form['password']
        f = request.files['file']
        f.save(f"static/img/{image}.jpg")
        description = request.form['about']
        price = request.form['price']
        product = Foodshare(
            name=email, contacts=password, description=description, image=image, confirmed=0, price=price)
        session.add(product)
        session.commit()
        return redirect('/order')


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


@app.route('/adm_panel', methods=['GET', 'POST'])
def administrate():
    if request.method == 'POST':
        print(request.form['submit'])
        id = int(request.form['submit'].split("-")[1])

        if "add" in request.form['submit']:
            action_card = session.query(Foodshare).filter_by(id=id).one()
            action_card.confirmed = 1
            session.add(action_card)
            session.commit()
        else:
            to_delete = session.query(Foodshare).filter_by(id=id).one()
            session.delete(to_delete)
            session.commit()

        test_page = []
        if not session.query(Foodshare).filter_by(confirmed=0).first():
            for i in session.query(Foodshare).filter_by(confirmed=0).all():
                image = f"static/img/{i.image}.jpg"
                test_page.append(
                    render_template(
                        "admin_card.html", name=i.name, price=i.price, description=i.description, image=image, id=i.id))
                session.commit()
            return render_template('admin_panel.html').format(' '.join(test_page))

    else:
        if not session.query(Foodshare).filter_by(confirmed=0).first():
            test_page = []
            for i in session.query(Foodshare).filter_by(confirmed=0).all():
                image = f"static/img/{i.image}.jpg"
                test_page.append(
                    render_template(
                        "admin_card.html", name=i.name, price=i.price, description=i.description, image=image, id=i.id))
                session.commit()
            return render_template('admin_panel.html').format(' '.join(test_page))


if __name__ == '__main__':
    if debug:
        app.run(port=8080, host="127.0.0.1")
    else:
        app.run()
