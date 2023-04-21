import os
from flask import Flask, render_template, request, redirect, url_for, make_response
from flask import session


app = Flask(__name__)
app.secret_key = os.urandom(24)

def check_admin(username):
    return username == "andrewmohawk"

def get_users():
    with open('users.txt', 'r') as f:
        return [line.strip().split(':') for line in f.readlines()]

def get_posts():
    lines = []
    with open('posts.txt', 'r') as f:
        lines = f.readlines()
    # reverse the lines so the most recent post is first
    lines.reverse()
    return lines

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None

        for user in get_users():
            if user[0] == username and user[1] == password:
                response = make_response(redirect(url_for("user_page")))
                response.set_cookie("admin", "1" if check_admin(username) else "0")
                session["username"] = username
                return response

        error = f"Invalid credentials for user {username}"
        return render_template("login.html", error=error)

    return render_template("login.html")

@app.route("/user_page")
def user_page(error=None):
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))

    admin = request.cookies.get("admin")
    session_data = request.cookies.get(app.config["SESSION_COOKIE_NAME"])
    return render_template("user_page.html", username=username, admin=admin, session=session_data, users=get_users(), posts=get_posts(),error=error)

@app.route("/new_post", methods=["POST"])
def new_post():
    username = session.get("username")
    if not username:
        return redirect(url_for("login"))

    
    admin = request.cookies.get("admin")

    if not check_admin(username):
        return user_page(error="Only administrators can post")

    post = request.form["post"]
    with open('posts.txt', 'a') as f:
        f.write(post + "\n")

    return redirect(url_for("user_page"))

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("login")))
    response.set_cookie("session", "", expires=0)
    return response

if __name__ == "__main__":
    app.run(debug=True)
