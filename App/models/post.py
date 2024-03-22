from App.database import db
from App.models.user import User

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    text = db.Column(db.String)

    def __init__(self, userId, text):
        self.userId = userId
        self.text = text

    def getTotalLikes(self):
        return UserReact.query.filter_by(postId=self.id, react='like').count()

    def getTotalDislikes(self):
        return UserReact.query.filter_by(postId=self.id, react='dislike').count()

    def toDict(self):
        author = User.query.get(self.userId)
        return {
            'id': self.id,
            'userId': self.userId,
            'text': self.text,
            'username': author.username,
            'likes': self.getTotalLikes(),
            'dislikes': self.getTotalDislikes()
        }
