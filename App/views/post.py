from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from.index import index_views

from App.controllers import (
    create_user,
    get_all_users,
    get_all_users_json,
    jwt_required,
    add_auth_context
)

post_views = Blueprint('post_views', __name__, template_folder='../templates')

@post_views.route('/post', methods=['GET'])
@jwt_required()
def get_shop_page():
    
    return render_template('post.html', current_user=jwt_current_user)
