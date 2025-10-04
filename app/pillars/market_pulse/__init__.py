from flask import Blueprint, render_template, jsonify
# from flask_login import login_required  # COMMENT OUT
import requests
import os

bp = Blueprint('market_pulse', __name__)

@bp.route('/')
# @login_required  # COMMENT OUT
def market_dashboard():
    return render_template('market_pulse_dashboard.html')  # Fixed template name

@bp.route('/quotes/<symbols>')
def get_quotes(symbols):
    # Mock market data
    mock_data = {
        'AAPL': {'price': 185.43, 'change': 1.23, 'changePercent': 0.67},
        'MSFT': {'price': 374.58, 'change': -0.45, 'changePercent': -0.12},
        'GOOGL': {'price': 138.21, 'change': 2.34, 'changePercent': 1.72},
        'VTI': {'price': 234.56, 'change': 0.78, 'changePercent': 0.33},
        'BND': {'price': 78.90, 'change': -0.12, 'changePercent': -0.15},
        'QQQ': {'price': 389.12, 'change': 3.45, 'changePercent': 0.89},
        'ARKK': {'price': 45.67, 'change': 1.23, 'changePercent': 2.77}
    }

    symbol_list = symbols.split(',')
    quotes = {
        symbol.upper(): mock_data[symbol.upper()]
        for symbol in symbol_list
        if symbol.upper() in mock_data
    }
    return jsonify(quotes)