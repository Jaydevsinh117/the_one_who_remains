from flask import Blueprint, request, jsonify
from models.blog_model import Blog
from app import db

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/api/blog', methods=['POST'])
def add_blog():
    data = request.json

    if not data.get('title') or not data.get('content'):
        return jsonify({"error": "Missing required fields"}), 400

    blog = Blog(
        title=data['title'],
        content=data['content']
    )

    try:
        db.session.add(blog)
        db.session.commit()
        return jsonify({"message": "Blog added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
