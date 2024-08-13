import os
import smtplib
from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import html

load_dotenv()

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html", page_name="Contact Me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/form_entry", methods=["POST"])
def send_entry():
    with smtplib.SMTP(host=os.getenv("SMTP_HOST"), port=587) as smtp:
        smtp.starttls()
        smtp.login(user=os.getenv("SMTP_USER"), password=os.getenv("SMTP_PASSWORD"))

        smtp.sendmail(from_addr=os.getenv("SMTP_USER"), to_addrs="YOUR_EMAIL",
                      msg=f"Subject:New Message\n\n"
                          f"Name:{html.unescape(request.form["name"])}\n"
                          f"Email:{html.unescape(request.form["email"])}\n"
                          f"Phone:{html.unescape(request.form["phone"])}\n"
                          f"Message:{html.unescape(request.form["message"])}\n")
        smtp.close()

    return render_template("contact.html", page_name="Successfully sent message")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
