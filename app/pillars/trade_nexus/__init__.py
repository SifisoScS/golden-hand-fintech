from flask import Blueprint, render_template, jsonify, request
# from flask_login import login_required, current_user  # COMMENT OUT
from app.models import Transaction, Portfolio, db
from datetime import datetime

bp = Blueprint('trade_nexus', __name__)

@bp.route('/')
# @login_required  # COMMENT OUT
def trading_desk():
    # TEMPORARY: Demo portfolios instead of user portfolios
    # portfolios = current_user.portfolios.all()
    demo_portfolios = [
        {'id': 1, 'name': 'Growth Portfolio'},
        {'id': 2, 'name': 'Retirement Fund'},
        {'id': 3, 'name': 'Emergency Fund'}
    ]
    return render_template('trade_nexus_dashboard.html', portfolios=demo_portfolios)

@bp.route('/execute', methods=['POST'])
# @login_required  # COMMENT OUT
def execute_trade():
    data = request.json
    
    # TEMPORARY: Skip authentication and database saving
    # portfolio = Portfolio.query.get(data['portfolio_id'])
    # if portfolio.owner != current_user:
    #     return jsonify({'success': False, 'error': 'Unauthorized'})
    
    # Create demo transaction response
    demo_transaction = {
        'id': 999,
        'symbol': data.get('symbol', 'AAPL'),
        'type': data.get('type', 'buy'),
        'quantity': data.get('quantity', 10),
        'price': data.get('price', 185.43),
        'timestamp': datetime.utcnow().isoformat()
    }
    
    return jsonify({'success': True, 'transaction': demo_transaction, 'message': 'Demo mode - trade simulated'})