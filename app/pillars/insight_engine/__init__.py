from flask import Blueprint, render_template, jsonify
from flask_login import login_required, current_user
from app.models import Transaction, Portfolio
from datetime import datetime, timedelta

bp = Blueprint('insight_engine', __name__)

@bp.route('/')
@login_required
def analytics_dashboard():
    return render_template('insight_engine/dashboard.html')

@bp.route('/portfolio-performance')
@login_required
def portfolio_performance():
    # Mock performance data - integrate with real analytics
    portfolios = current_user.portfolios.all()
    performance_data = []

    performance_data.extend(
        {
            'name': portfolio.name,
            'value': 10000 + len(portfolio.holdings.all()) * 1000,
            'dailyChange': 2.5,
            'totalReturn': 15.7,
        }
        for portfolio in portfolios
    )
    return jsonify(performance_data)

@bp.route('/transaction-history')
@login_required
def transaction_history():
    transactions = current_user.transactions.order_by(Transaction.timestamp.desc()).limit(10).all()
    history = [{
        'symbol': t.symbol,
        'type': t.transaction_type,
        'quantity': t.quantity,
        'price': t.price,
        'timestamp': t.timestamp.isoformat()
    } for t in transactions]
    
    return jsonify(history)