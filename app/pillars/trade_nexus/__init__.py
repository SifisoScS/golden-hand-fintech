from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Transaction, Portfolio, db
from datetime import datetime

bp = Blueprint('trade_nexus', __name__)

@bp.route('/')
@login_required
def trading_desk():
    portfolios = current_user.portfolios.all()
    return render_template('trade_nexus/desk.html', portfolios=portfolios)

@bp.route('/execute', methods=['POST'])
@login_required
def execute_trade():
    data = request.json
    portfolio = Portfolio.query.get(data['portfolio_id'])
    
    if portfolio.owner != current_user:
        return jsonify({'success': False, 'error': 'Unauthorized'})
    
    # Create transaction
    transaction = Transaction(
        user_id=current_user.id,
        portfolio_id=portfolio.id,
        symbol=data['symbol'],
        transaction_type=data['type'],
        quantity=data['quantity'],
        price=data['price']
    )
    
    db.session.add(transaction)
    db.session.commit()
    
    return jsonify({'success': True, 'transaction_id': transaction.id})