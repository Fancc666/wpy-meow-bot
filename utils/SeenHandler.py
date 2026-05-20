import sqlite3
from pathlib import Path

conn = sqlite3.connect(Path(__file__).parent / "seen.db")

# 初始化
conn.execute("CREATE TABLE IF NOT EXISTS seen_posts (post_id TEXT PRIMARY KEY, seen_at TEXT)")
conn.commit()

# 已回复帖子的去重
def get_new_replys(current_replys):
    new_replys = []
    for post in current_replys:
        post_id = post['id']
        # 检查是否已处理过
        cur = conn.execute("SELECT 1 FROM seen_posts WHERE post_id = ?", (post_id,))
        if cur.fetchone() is None:
            new_replys.append(post)
            conn.execute("INSERT INTO seen_posts (post_id, seen_at) VALUES (?, datetime('now'))", (post_id,))
    conn.commit()
    return new_replys
