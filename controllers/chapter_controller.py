from flask import Blueprint, request, jsonify
from models.chapter_model import Chapter
from app import db

chapter_bp = Blueprint('chapter', __name__)

@chapter_bp.route('/api/chapter', methods=['POST'])
def add_chapter():
    data = request.json

    if not data.get('name') or not data.get('content'):
        return jsonify({"error": "Missing required fields"}), 400

    chapter = Chapter(
        name=data['name'],
        content=data['content']
    )

    try:
        db.session.add(chapter)
        db.session.commit()
        return jsonify({"message": "Chapter added successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
