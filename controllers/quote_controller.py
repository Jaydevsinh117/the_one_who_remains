from flask import Blueprint, request, jsonify
from models.quote_model import Quote

quote_bp = Blueprint('quote', __name__)

@quote_bp.route('/api/quote', methods=['POST'])
def add_quote():
    from app import db  # Move the import here to avoid circular import
    
    data = request.json

    if not data.get('text') or not data.get('author'):
        return jsonify({"error": "Missing required fields"}), 400

    quote = Quote(
        text=data['text'],
        author=data['author']
    )

    try:
        db.session.add(quote)
        db.session.commit()
        return jsonify({"message": "Quote added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
