from flask import Flask, redirect, url_for
app = Flask(__name__)

app.config.from_object('config')


@app.route('/')
def index():
  return '<h1>Hello World!</h1>'


@app.route('/about-me')
def about_me():
  return redirect(url_for('about'))

if __name__ == '__main__':
  app.run()