from flask import Flask, render_template
from post import Post
from requests import get

def get_posts():
    posts = get("https://api.npoint.io/c790b4d5cab58020d391").json()
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return post_objects

posts = get_posts()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/post/<int:post_id>')
def get_post(post_id:int):
    requested_post = None
    for post in posts:
        if post.id == post_id:
            requested_post = post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
