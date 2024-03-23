from App.database import db

class UserReact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    react = db.Column(db.Enum('like', 'dislike'))

    def __init__(self, user_id, post_id, react):
        self.user_id = user_id
        self.post_id = post_id
        self.react = react

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'post_id': self.post_id,
            'react': self.react
        }