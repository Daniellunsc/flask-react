from flask import Flask, render_template, jsonify, request, json, Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models.user import User
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token
from flask_jwt_extended import set_access_cookies, set_refresh_cookies, get_jwt_identity, jwt_refresh_token_required
import datetime

Auth = Blueprint('Auth', __name__)

users = [
    User(1, 'user1', '1234'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

@Auth.route('/checkAuth')
@jwt_required
def checkAuth():
  return jsonify({'status' : 'true'}), 200

@Auth.route('/token/refresh')
@jwt_refresh_token_required
def refreshToken():
  current_user = get_jwt_identity()
  access_token = create_access_token(identity=current_user)
  refresh_token = create_refresh_token(identity=current_user)
  resp = jsonify({'refresh': True})
  set_access_cookies(resp, access_token)
  set_refresh_cookies(resp, refresh_token)
  return resp

@Auth.route('/auth', methods=['GET', 'POST'])
def auth():
  data = request.data
  dataDict = json.loads(data)
  user = username_table.get(dataDict['username'])
  if user:
    access_token = create_access_token(identity = user.username)
    refresh_token = create_refresh_token(identity = user.username)
    resp = jsonify({'status': 'success'})
    set_access_cookies(resp, access_token)
    set_refresh_cookies(resp, refresh_token)
  else:
    resp = jsonify(status="failure"), 401
  return resp