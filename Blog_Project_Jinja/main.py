import requests
from post import Post
from flask import Flask, render_template

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    selected_post = [_post for _post in post_objects if _post.id == post_id][0]
    return render_template('post.html', post=selected_post)

if __name__ == "__main__":
    app.run(debug=True)
