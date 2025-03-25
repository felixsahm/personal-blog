from flask import Flask, redirect, url_for, render_template, send_file
app = Flask(__name__)

app.config.from_object('app.config')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts')
def posts():
  return render_template('posts.html')

@app.route('/posts/<slug>')
def posts_slug(slug):
  return render_template('posts-slug.html', slug=slug)

@app.route('/about')
def about():
  return render_template('about.html')

#test if i see this
#another test if i see that