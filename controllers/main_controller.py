import secrets

from flask import abort, redirect, render_template, request, session, url_for
from sqlalchemy import and_, or_

from app import db
from models import Highscore


class MainController:
    @staticmethod
    def _highscore_pagination(page):
        page = max(page or 1, 1)
        query = Highscore.query.order_by(Highscore.attempts.asc(), Highscore.id.asc())
        pagination = query.paginate(page=page, per_page=10, error_out=False)
        if pagination.pages and page > pagination.pages:
            pagination = query.paginate(page=pagination.pages, per_page=10, error_out=False)
        return pagination

    @staticmethod
    def index():
        session.clear()
        pagination = MainController._highscore_pagination(request.args.get('page', 1, type=int))
        return render_template(
            'index.html',
            highscores=pagination.items,
            pagination=pagination
        )

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
        required_session_keys = ('player_name', 'attempts', 'highlighted_highscore_id')
        if any(key not in session for key in required_session_keys):
            return redirect(url_for('index'))
        highlighted_highscore_id = session['highlighted_highscore_id']
        highlighted_score = db.session.get(Highscore, highlighted_highscore_id)
        if highlighted_score is None:
            abort(404)

        rank = Highscore.query.filter(
            or_(
                Highscore.attempts < highlighted_score.attempts,
                and_(
                    Highscore.attempts == highlighted_score.attempts,
                    Highscore.id <= highlighted_score.id
                )
            )
        ).count()
        highlighted_page = (rank - 1) // 10 + 1
        requested_page = request.args.get('page', type=int)
        pagination = MainController._highscore_pagination(
            requested_page if requested_page is not None else highlighted_page
        )
        return render_template(
            'win.html',
            player_name=session['player_name'],
            attempts=session['attempts'],
            target_number=session['target_number'],
            highscores=pagination.items,
            pagination=pagination,
            highlighted_highscore_id=highlighted_highscore_id
        )
