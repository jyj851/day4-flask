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
    per_page = 10
    page = request.args.get("page", 1, type=int) or 1
    page = max(page, 1)
    q = (request.args.get("q") or "").strip()
    sort = request.args.get("sort", "new")

    sort_orders = {
        "new": "created_at DESC",
        "old": "created_at ASC",
        "title": "title COLLATE NOCASE ASC",
    }
    if sort not in sort_orders:
        sort = "new"
    order_by = sort_orders[sort]

    conn = get_db()
    if q:
        like_q = f"%{q}%"
        total_posts = conn.execute(
            "SELECT COUNT(*) FROM posts WHERE title LIKE ? OR content LIKE ?",
            (like_q, like_q),
        ).fetchone()[0]
    else:
        total_posts = conn.execute("SELECT COUNT(*) FROM posts").fetchone()[0]

    total_pages = (total_posts + per_page - 1) // per_page if total_posts else 1
    page = min(page, total_pages)
    offset = (page - 1) * per_page

    if q:
        like_q = f"%{q}%"
        rows = conn.execute(
            f"SELECT * FROM posts WHERE title LIKE ? OR content LIKE ? ORDER BY {order_by} LIMIT ? OFFSET ?",
            (like_q, like_q, per_page, offset),
        ).fetchall()
    else:
        rows = conn.execute(
            f"SELECT * FROM posts ORDER BY {order_by} LIMIT ? OFFSET ?",
            (per_page, offset),
        ).fetchall()

    conn.close()

    posts = [parse_post(r) for r in rows]
    return render_template(
        "list.html",
        posts=posts,
        page=page,
        total_pages=total_pages,
        q=q,
        has_search=bool(q),
        sort=sort,
    )


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


@app.route("/edit/<int:post_id>", methods=["GET", "POST"])
def post_edit(post_id):
    conn = get_db()
    if request.method == "POST":
        conn.execute(
            "UPDATE posts SET title=?, content=? WHERE id=?",
            (request.form["title"], request.form["content"], post_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("post_detail", post_id=post_id))
    row = conn.execute("SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    conn.close()
    if row is None:
        return redirect(url_for("post_list"))
    return render_template("create.html", post=parse_post(row), editing=True)


@app.route("/delete/<int:post_id>", methods=["POST"])
def post_delete(post_id):
    conn = get_db()
    conn.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("post_list"))


with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True)
