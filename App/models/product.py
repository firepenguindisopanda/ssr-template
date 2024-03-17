from App.database import db
import datetime

class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  date_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  category = db.Column(db.String(120))
  price = db.Column(db.Float, nullable=False)
  image = db.Column(db.String(120))
  about = db.Column(db.String(120))
  cart = db.relationship('Cart', backref='product', lazy=True)

  def __init__(self, name, category, price, image, about):
    self.name = name
    self.category = category
    self.price = price
    self.image = image
    self.about = about

  def __repr__(self):
    return f"Product('{self.name}', '{self.category}', '{self.price}', '{self.image}', '{self.about}')"

  def toDict(self):
    return {
        'id': self.id,
        'name': self.name,
        'category': self.category,
        'price': self.price,
        'image': self.image,
        'about': self.about
    }

  def get_id(self):
    return self.id