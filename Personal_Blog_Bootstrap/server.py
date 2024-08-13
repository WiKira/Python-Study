import requests
from datetime import datetime
from flask import Flask, render_template

from post import Post

app = Flask(__name__)

ALL_POSTS = requests.get('https://api.npoint.io/1ac6b71368f2befdb1cb').json()
POSTS_LIST = []
for post in ALL_POSTS:
    post["date"] = datetime.strptime(post["date"], "%Y-%m-%d").strftime("%B %d, %Y")

    new_post = Post(post["id"],
                    post["title"],
                    post["subtitle"],
                    post["date"],
                    post["author"],
                    post["img_link"],
                    post["body"])

    POSTS_LIST.append(new_post)


@app.route('/')
def home_page():
    return render_template("index.html",
                           title="Clean Blog",
                           subtitle="A Blog Theme by Start Bootstrap",
                           bg_img="static/assets/img/home-bg.jpg",
                           all_posts=POSTS_LIST)


@app.route('/contact')
def contact_page():
    return render_template("contact.html",
                           title="Contacts",
                           subtitle="Have questions? I have answers.",
                           bg_img="static/assets/img/contact-bg.jpg")


@app.route('/about')
def about_page():
    return render_template("about.html",
                           title="About Me",
                           subtitle="This is what I do.",
                           bg_img="static/assets/img/about-bg.jpg")

@app.route('/post/<int:post_id>')
def post_page(post_id):
    selected_post = None
    for post_in_list in POSTS_LIST:
        if post_in_list.id == post_id:
            selected_post = post_in_list
            break

    return render_template("post.html",
                           title=selected_post.title,
                           subtitle=selected_post.subtitle,
                           bg_img=selected_post.img_link,
                           post=selected_post)


if __name__ == '__main__':
    app.run(debug=True)
