# controllers/user_controller.py

from flask import Blueprint, request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from models.user_model import User
import uuid

user_bp = Blueprint('user', __name__)

@user_bp.route('/register')
def register_page():
    return render_template('register.html')

@user_bp.route('/api/register', methods=['POST'])
def register():
    from app import db  # Import db here to avoid circular import

    data = request.json

    # Input validation
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists"}), 400

    hashed_password = generate_password_hash(data['password'])
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=hashed_password
    )

    try:
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
