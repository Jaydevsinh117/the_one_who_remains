from flask import Blueprint, request, jsonify
from models.product_model import Product

product_bp = Blueprint('product', __name__)

@product_bp.route('/api/product', methods=['POST'])
def add_product():
    from app import db  # Move the import here to avoid circular import
    
    data = request.json

    if not data.get('name') or not data.get('price'):
        return jsonify({"error": "Missing required fields"}), 400

    product = Product(
        name=data['name'],
        description=data.get('description', ''),
        price=data['price']
    )

    try:
        db.session.add(product)
        db.session.commit()
        return jsonify({"message": "Product added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
