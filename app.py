from flask import Flask, redirect, url_for, render_template, send_file
app = Flask(__name__)

app.config.from_object('config')


cookies_data = [ #list
  {'name': 'Chocolate Chip', 'price': '$1.50'},
  {'name': 'Oatmeal Raisin', 'price': '$1.00'},
  {'name': 'Sugar', 'price': '$0.75'},
  {'name': 'Peanut Butter', 'price': '$0.50'},
  {'name': 'Oatmeal', 'price': '$0.25'},
  {'name': 'Salted Caramel', 'price': '$1.00'},
]

@app.route('/cookies/<int:id>')
def cookie(id):
  return '<h1>' + cookies_data[id]['name'] + '</h1>' + '<p>' + cookies_data[id]['price'] + '</p>'

@app.route('/index.html')
def index():
  return render_template('index.html')

@app.route('/posts.html')
def posts():
  return render_template('posts.html')

@app.route('/about.html')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run()