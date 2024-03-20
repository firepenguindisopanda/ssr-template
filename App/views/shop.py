from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required,
    get_all_products,
    get_cart_items,
    get_cart_total,
    update_cart_item,
    product_search,
    add_to_cart,
    remove_from_cart,
    get_cart_items_with_product_info,
    add_auth_context
)

shop_views = Blueprint('shop_views', __name__, template_folder='../templates')

@shop_views.route('/shop', methods=['GET'])
def get_shop_page():
    products = get_all_products()
    # cart_items_to_display = [cart_items.toDict() for cart_items in get_cart_items()]
    cart_items_to_display = get_cart_items_with_product_info()
    cart_total = "{:.2f}".format(get_cart_total())
    
    # this shows a proof of concept of how to retrieve product details using the product_id from cart object
    # for cart_it in get_cart_items():
    #     print(cart_it.product.name)
    return render_template('shop_app.html', products=products, cart_items_to_display=cart_items_to_display,cart_total=cart_total)

@shop_views.route('/cart/add', methods=['POST'])
def add_to_cart_route():
    product_id = request.form.get('product_id')
    add_to_cart(product_id)
    flash('Product added to cart successfully!')
    return redirect(url_for('shop_views.get_shop_page'))

# @shop_views.route('/cart/update', methods=['POST'])
# def update_cart_route():
#     cart_item_id = request.form.get('cart_item_id')
#     quantity = int(request.form.get('quantity'))
#     update_cart_item(cart_item_id, quantity)
#     flash('Cart updated successfully!')
#     return redirect(url_for('shop_views.get_shop_page'))

@shop_views.route('/cart/remove', methods=['POST'])
def remove_from_cart_route():
    cart_item_id = request.form.get('cart_item_id')
    remove_from_cart(cart_item_id)
    flash('Product removed from cart successfully!')
    return redirect(url_for('shop_views.get_shop_page'))

@shop_views.route('/cart/update', methods=['POST'])
def update_cart_route():
    cart_item_id = request.form.get('cart_item_id')
    quantity = int(request.form.get('quantity'))
    
    # Ensure quantity is not negative
    if quantity < 0:
        quantity = 0
    
    # Update the cart item or remove it if quantity is 0
    if quantity == 0:
        remove_from_cart(cart_item_id)
    else:
        update_cart_item(cart_item_id, quantity)
    
    flash('Cart updated successfully!')
    return redirect(url_for('shop_views.get_shop_page'))
