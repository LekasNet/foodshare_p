from flask import Flask, render_template, url_for


app = Flask(__name__, static_folder="static")


@app.route('/')
def welcome():
    return render_template("main_page.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')