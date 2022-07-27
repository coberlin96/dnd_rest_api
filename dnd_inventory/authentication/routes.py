from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from dnd_inventory.models import User, db, check_password_hash, user_schema
# from dnd_inventory.forms import UserLoginForm

from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__, url_prefix= '/auth')

@auth.route('/signup', methods = ['POST'])
def signup():
    email = request.json['email']
    password = request.json['password']
    g_auth_verify = request.json['g_auth_verify']
    
    user = User(email, password=password, g_auth_verify=g_auth_verify)

    db.session.add(user)
    db.session.commit()

    response = user_schema.dump(user)

    return jsonify(response)

# @auth.route('/signup', methods = ['GET'])
# def retrieve(email):
#     User.query.get(email)



# @api.route('/stats/<id>', methods = ['GET'])
# @token_required
# def get_stats(current_user_token, id):
#     owner = current_user_token.token
#     if owner == current_user_token.token:
#         stats = Stats.query.get(id)
#         response = stats_schema.dump(stats)
#         return jsonify(response)
#     else:
#         return jsonify({'message': "Valid Token Required"}), 401