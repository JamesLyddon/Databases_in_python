from lib.post import Post

class PostRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []
        for row in rows:
            item = Post(row["id"], row["title"], row["content"], row["view_count"], row["user_id"])
            posts.append(item)
        return posts
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM posts WHERE id = %s', [id])
        row = rows[0]
        return Post(row["id"], row["title"], row["content"], row["view_count"], row["user_id"])
    
    def create(self, post):
        self._connection.execute('INSERT INTO posts (title, content, view_count, user_id) VALUES (%s, %s, %s, %s)', [post.title, post.content, post.view_count, post.user_id])
        return None
    
    def delete(self, post_id):
        self._connection.execute(
            'DELETE FROM posts WHERE id = %s', [post_id])
        return None