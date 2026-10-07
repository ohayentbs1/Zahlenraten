from Controllers.MainController import MainController

def register_routes(app):
    @app.route('/')
    def index():
        return MainController.index()

    @app.route('/start-game', methods=['POST'])
    def start_game():
        return MainController.start_game()

    @app.route('/game', methods=['GET', 'POST'])
    def game():
        return MainController.game()

    @app.route('/win', methods=['GET'])
    def win():
        return MainController.win()

    @app.route('/new-try', methods=['POST'])
    def new_try():
        return MainController.new_try()