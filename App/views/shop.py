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
    search_products,
    add_to_cart,
    remove_from_cart,
    add_auth_context
)

shop_views = Blueprint('shop_views', __name__, template_folder='../templates')

@shop_views.route('/shop', methods=['GET'])
def get_shop_page():
    cart_items = [
        {
            "cart":[
                {
                    "id":10,
                    "name":"Schylling Veterinarian Kit",
                    "price":9.39,
                    "product_id":19,
                    "quantity":5
                },
                {
                    "id":11,
                    "name":"Electronic Snap Circuits Mini Kits Classpack, FM Radio, Motion Detector, Music Box (Set of 5)",
                    "price":99.95,
                    "product_id":2,
                    "quantity":3
                },
                {
                    "id":12,
                    "name":"DB Longboards CoreFlex Crossbow 41\" Bamboo Fiberglass Longboard Complete",
                    "price":237.68,
                    "product_id":1,
                    "quantity":1
                }
            ],
            "total":584.48
        }
    ]

    products = [
        {
                    "id":10,
                    "name":"Schylling Veterinarian Kit",
                    "price":9.39,
                    "product_id":19,
                    "quantity":5
                },
                {
                    "id":11,
                    "name":"Electronic Snap Circuits Mini Kits Classpack, FM Radio, Motion Detector, Music Box (Set of 5)",
                    "price":99.95,
                    "product_id":2,
                    "quantity":3
                },
                {
                    "id":12,
                    "name":"DB Longboards CoreFlex Crossbow 41\" Bamboo Fiberglass Longboard Complete",
                    "price":237.68,
                    "product_id":1,
                    "quantity":1
                }
    ]
    cart_items_to_display = cart_items[0]
    return render_template('shop_app.html', products=products, cart_items=cart_items_to_display)