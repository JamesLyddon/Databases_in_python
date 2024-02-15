from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users')
        users = []
        for row in rows:
            item = User(row["id"], row["name"], row["email"])
            users.append(item)
        return users
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM users WHERE id = %s', [id])
        row = rows[0]
        return User(row["id"], row["name"], row["email"])
    
    def create(self, user):
        self._connection.execute('INSERT INTO users (name, email) VALUES (%s, %s)', [user.name, user.email])
        return None
    
    def delete(self, user_id):
        self._connection.execute(
            'DELETE FROM users WHERE id = %s', [user_id])
        return None