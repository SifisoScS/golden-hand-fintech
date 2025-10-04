from flask import Blueprint, render_template, jsonify
# from flask_login import login_required, current_user  # COMMENT OUT
from app.models import Transaction, Portfolio
from datetime import datetime, timedelta

bp = Blueprint('insight_engine', __name__)

@bp.route('/')
# @login_required  # COMMENT OUT
def analytics_dashboard():
    return render_template('insight_engine_dashboard.html')  # Fixed template name

@bp.route('/portfolio-performance')
# @login_required  # COMMENT OUT
def portfolio_performance():
    # Mock performance data
    performance_data = [
        {
            'name': 'Growth Portfolio',
            'value': 45230.15,
            'dailyChange': 2.5,
            'totalReturn': 15.7,
            'riskScore': 6.8
        },
        {
            'name': 'Retirement Fund', 
            'value': 125000.00,
            'dailyChange': 1.2,
            'totalReturn': 8.3,
            'riskScore': 4.2
        },
        {
            'name': 'Emergency Fund',
            'value': 15000.00, 
            'dailyChange': 0.3,
            'totalReturn': 2.1,
            'riskScore': 2.1
        }
    ]
    
    return jsonify(performance_data)

@bp.route('/transaction-history')
# @login_required  # COMMENT OUT
def transaction_history():
    # Mock transaction history
    demo_transactions = [
        {
            'symbol': 'AAPL',
            'type': 'buy',
            'quantity': 10,
            'price': 185.43,
            'timestamp': (datetime.utcnow() - timedelta(hours=2)).isoformat()
        },
        {
            'symbol': 'MSFT',
            'type': 'buy', 
            'quantity': 5,
            'price': 374.58,
            'timestamp': (datetime.utcnow() - timedelta(days=1)).isoformat()
        },
        {
            'symbol': 'VTI',
            'type': 'buy',
            'quantity': 25,
            'price': 234.56,
            'timestamp': (datetime.utcnow() - timedelta(days=3)).isoformat()
        }
    ]
    
    return jsonify(demo_transactions)