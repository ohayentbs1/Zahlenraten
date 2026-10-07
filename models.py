from datetime import datetime
from app import db

class Highscore(db.Model):
    __tablename__ = 'highscores'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
