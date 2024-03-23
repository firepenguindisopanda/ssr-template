from App.database import db
from App.models.user import User

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String)
    reactions = db.relationship('UserReact', backref='post', cascade='all,delete', lazy=True)

    def __init__(self, user_id, text):
        self.user_id = user_id
        self.text = text

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'text': self.text,
            'username': self.author.username,
            'likes': self.get_total_likes(),
            'dislikes': self.get_total_dislikes()
        }

    def get_total_likes(self):
        return UserReact.query.filter_by(post_id=self.id, react='like').count()

    def get_total_dislikes(self):
        return UserReact.query.filter_by(post_id=self.id, react='dislike').count()
