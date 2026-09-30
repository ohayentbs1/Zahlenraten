from Controllers.GameController import GameController
from Controllers.HighscoreController import HighscoreController


def register_routes(app):
    @app.route('/')
    def index():
        return HighscoreController.index()

    @app.route('/start-game', methods=['POST'])
    def start_game():
        return GameController.start_game()

    @app.route('/game', methods=['GET', 'POST'])
    def game():
        return GameController.game()
