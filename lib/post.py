class Post:
    def __init__(self, id, title, content, view_count, user_id):
        self.id = id
        self.title = title
        self.content = content
        self.view_count = view_count
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content}, {self.view_count}, {self.user_id})"