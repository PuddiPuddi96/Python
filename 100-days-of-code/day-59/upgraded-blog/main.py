from flask import Flask, render_template
from post import Post
from requests import get

def get_posts():
    posts = get("https://api.npoint.io/3a74d1849e973ce66263").json()
    post_objects = []
    for post in posts:
        post_obj = Post(
            post["id"], 
            post["title"], 
            post["subtitle"], 
            post["body"],
            post["author"],
            post["date"],
            post["image_url"])
        post_objects.append(post_obj)
    return post_objects

posts = get_posts()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def get_post(post_id:int):
    post_to_render = None
    for post in posts:
        if post.id == post_id:
            post_to_render = post
    return render_template('post.html', post=post_to_render)

@app.route('/about')
def get_about_page():
    return render_template('about.html')

@app.route('/contact')
def get_contact_page():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
