from flask import Blueprint, request, jsonify, session
from models.admin_model import Admin

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/api/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    admin = Admin.query.filter_by(username=data['username']).first()
    
    if admin and admin.password == data['password']:  # In production, hash the password
        session['admin'] = True
        return jsonify({"message": "Admin login successful"}), 200
    return jsonify({"error": "Invalid admin credentials"}), 401
