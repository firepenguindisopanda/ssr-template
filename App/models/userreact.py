from App.database import db

class UserReact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    postId = db.Column(db.Integer)
    react = db.Column(db.Enum('like', 'dislike'))

    def __init__(self, userId, postId, react):
        self.userId = userId
        self.postId = postId
        self.react = react

    def to_dict(self):
        return {
            'id': self.id,
            'userId': self.userId,
            'postId': self.postId,
            'react': self.react
        }