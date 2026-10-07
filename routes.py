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

    @app.route('/win', methods=['GET'])
    def win():
        return GameController.win()

    @app.route('/new-try', methods=['POST'])
    def new_try():
        return GameController.new_try()