from app import db

class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Quote {self.text}>'
