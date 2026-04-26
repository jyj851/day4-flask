import sqlite3
import sys
from pathlib import Path

import requests

from crawler import LIMIT, RSS_URL, fetch_news

DATABASE = str(Path(__file__).with_name("journal.db"))


def ensure_posts_table(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )


def build_content(item: dict) -> str:
    summary = item.get("summary", "")
    link = item.get("link", "")
    pub_date = item.get("pub_date", "")
    return f"{summary}\n\n링크: {link}\n발행시간: {pub_date}".strip()


def seed_posts(database_path: str | None = None) -> int:
    try:
        news_items = fetch_news(RSS_URL, LIMIT)
    except requests.RequestException as e:
        print(f"RSS 조회 실패: {e}")
        return 0

    conn = sqlite3.connect(database_path or DATABASE)
    ensure_posts_table(conn)

    added_count = 0
    for item in news_items:
        title = (item.get("title") or "").strip()
        if not title:
            continue

        exists = conn.execute(
            "SELECT 1 FROM posts WHERE title = ? LIMIT 1",
            (title,),
        ).fetchone()

        if exists:
            continue

        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, build_content(item)),
        )
        added_count += 1

    conn.commit()
    conn.close()
    return added_count


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    inserted = seed_posts()
    print(f"{inserted}건 추가됨")


if __name__ == "__main__":
    main()
