from App.database import db
import datetime

class Cart(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  quantity = db.Column(db.Integer, nullable=False)
  date_added = db.Column(db.DateTime, default=datetime.datetime.utcnow)
  product_id = db.Column(db.Integer,
                         db.ForeignKey('product.id'),
                         nullable=False)

  def __init__(self, quantity, product_id):
    self.quantity = quantity
    self.product_id = product_id

  def __repr__(self):
    return f"Cart('{self.quantity}', '{self.product_id}')"

  def toDict(self):
    return {
        'id': self.id,
        'quantity': self.quantity,
        'date_added': self.date_added,
        'product_id': self.product_id
    }