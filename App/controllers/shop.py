from App.models import Product, Cart
from App.database import db

def create_new_product(name,category,price,image,about):
    newproduct = Product(name=name,category=category,price=price,image=image,about=about)
    # db.session.add(newproduct)
    # db.session.commit()
    return newproduct

def get_all_products():
    """Retrieves all products from the database."""
    return Product.query.all()

def search_products(query):
    """Searches for products based on a given query."""
    return Product.query.filter(Product.name.ilike(f"%{query}%")).all()

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