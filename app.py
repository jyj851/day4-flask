import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATABASE = "journal.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


def parse_post(row):
    d = dict(row)
    if isinstance(d["created_at"], str):
        d["created_at"] = datetime.strptime(d["created_at"], "%Y-%m-%d %H:%M:%S")
    return d


@app.route("/")
def post_list():
    conn = get_db()
    rows = conn.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    posts = [parse_post(r) for r in rows]
    return render_template("list.html", posts=posts)


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    conn = get_db()
    row = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()
    if row is None:
        return redirect(url_for("post_list"))
    return render_template("detail.html", post=parse_post(row))


@app.route("/create", methods=["GET", "POST"])
def post_create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("post_list"))
    return render_template("create.html")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
