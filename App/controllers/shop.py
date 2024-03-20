from App.models import Product, Cart
from App.database import db
from sqlalchemy.orm import joinedload

def create_new_product(name,category,price,image,about):
    newproduct = Product(name=name,category=category,price=price,image=image,about=about)
    # db.session.add(newproduct)
    # db.session.commit()
    return newproduct

def get_all_products():
    """Retrieves all products from the database."""
    return Product.query.all()

def product_search(search):
  products = Product.query.filter(
      Product.name.like('%' + search + '%') |
      Product.about.like('%' + search + '%') |
      Product.category.like('%' + search + '%')
  ).all()
  return products

def add_to_cart(product_id, quantity=1):
    """Adds a product to the cart with the specified quantity."""
    cart_item = Cart.query.filter_by(product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(product_id=product_id, quantity=quantity)
        db.session.add(cart_item)
    db.session.commit()

def get_cart_items():
    """Retrieves all items currently in the cart."""
    return Cart.query.all()

def get_cart_items_with_product_info():
    """Retrieves all items currently in the cart along with product information."""
    cart_items = Cart.query.options(joinedload(Cart.product)).all()

    # Extract relevant information from each cart item and its associated product
    cart_items_with_product_info = []
    for cart_item in cart_items:
        product_info = {
            'id': cart_item.id,
            'quantity': cart_item.quantity,
            'date_added': cart_item.date_added,
            'product_id': cart_item.product.id,
            'name': cart_item.product.name,
            'price': cart_item.product.price,
            'image': cart_item.product.image,
            'about': cart_item.product.about
        }
        cart_items_with_product_info.append(product_info)
    return cart_items_with_product_info

def update_cart_item(cart_item_id, quantity):
    """Updates the quantity of a cart item."""
    cart_item = Cart.query.get(cart_item_id)
    if cart_item:
        cart_item.quantity = quantity
        db.session.commit()

def remove_from_cart(cart_item_id):
    """Removes an item from the cart."""
    cart_item = Cart.query.get(cart_item_id)
    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()

def get_cart_total():
    """Calculates and returns the total cost of items in the cart."""
    total = 0
    for item in get_cart_items():
        total += item.product.price * item.quantity
    return total