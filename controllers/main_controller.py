import secrets

from flask import abort, redirect, render_template, request, session, url_for

from app import db
from models import Highscore


class MainController:
    @staticmethod
    def index():
        session.clear()
        highscores = Highscore.query.order_by(Highscore.attempts.asc()).all()
        return render_template('index.html', highscores=highscores)

    @staticmethod
    def start_game():
        player_name = request.form.get('player_name', '').strip()
        if not player_name or len(player_name) > 80:
            abort(400, description='Der Spielername muss zwischen 1 und 80 Zeichen lang sein.')

        session.clear()
        session['player_name'] = player_name
        session['attempts'] = 0
        session['target_number'] = secrets.randbelow(100) + 1
        return redirect(url_for('game'))

    @staticmethod
    def game():
        if 'player_name' not in session or 'attempts' not in session:
            return redirect(url_for('index'))

        guess_result = None
        if request.method == 'POST':
            guess = request.form.get('guess', type=int)
            if guess is None or not 1 <= guess <= 100:
                abort(400, description='Die Zahl muss zwischen 1 und 100 liegen.')
            session['attempts'] += 1

            target_number = session['target_number']
            if guess > target_number:
                guess_result = 'Zu groß'
            elif guess < target_number:
                guess_result = 'zu klein'
            else:
                highscore = Highscore(
                    username=session['player_name'],
                    attempts=session['attempts'],
                )
                db.session.add(highscore)
                db.session.commit()
                session['highlighted_highscore_id'] = highscore.id
                return redirect(url_for('win'))

        return render_template(
            'game.html',
            player_name=session['player_name'],
            attempts=session['attempts'],
            target_number=session['target_number'],
            guess_result=guess_result
        )

    @staticmethod
    def new_try():
        player_name = session.get('player_name')
        if player_name is None:
            return redirect(url_for('index'))

        session.clear()
        session['player_name'] = player_name
        session['attempts'] = 0
        session['target_number'] = secrets.randbelow(100) + 1
        return redirect(url_for('game'))

    @staticmethod
    def win():
        if 'player_name' not in session or 'attempts' not in session:
            return redirect(url_for('index'))
        highscores = Highscore.query.order_by(Highscore.attempts.asc()).all()
        highlighted_highscore_id = session['highlighted_highscore_id']
        return render_template(
            'win.html',
            player_name=session['player_name'],
            attempts=session['attempts'],
            target_number=session['target_number'],
            highscores=highscores,
            highlighted_highscore_id=highlighted_highscore_id
        )