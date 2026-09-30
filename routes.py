from flask import render_template

from Controllers.GameController import GameController
from classes import Highscore


def register_routes(app):
    @app.route('/')
    def index():
        highscores = Highscore.query.order_by(Highscore.attempts.asc()).all()
        return render_template('index.html', highscores=highscores)

    @app.route('/start-game', methods=['POST'])
    def start_game():
        return GameController.start_game()

    @app.route('/game', methods=['GET', 'POST'])
    def game():
        return GameController.game()
