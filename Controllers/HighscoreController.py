from classes import Highscore
from flask import render_template, session


class HighscoreController:
    @staticmethod
    def index():
        session.clear()
        highscores = Highscore.query.order_by(Highscore.attempts.asc()).all()
        return render_template('index.html', highscores=highscores)