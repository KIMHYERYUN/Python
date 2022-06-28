import requests
from flask import Flask, render_template
from post import Post



post_url = "https://api.npoint.io/704c06f932b16ec2c902"

response = requests.get(post_url)
posts = response.json()
post_objects = []
for post in posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_object)


app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)


@app.route('/post/<int:index>')
def show_post(index):
    print(index)
    requested_post = None
    for post_objects_element in post_objects:
        if post_objects_element.id == index:
            requested_post = post_objects_element
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
