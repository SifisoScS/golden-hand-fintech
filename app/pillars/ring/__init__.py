from flask import Blueprint, jsonify
from .market_data.providers import MarketDataProvider
from .broker_apis.broker_interface import BrokerInterface

bp = Blueprint('ring', __name__)

market_data = MarketDataProvider()
broker_api = BrokerInterface()

@bp.route('/api/v1/integration/market/quotes/<symbols>')
def get_market_quotes(symbols):
    """Unified market data interface - standardized API contract"""
    quotes = market_data.get_quotes(symbols.split(','))
    return jsonify({
        'success': True,
        'data': quotes,
        'meta': {
            'timestamp': '2024-01-04T16:15:00Z',
            'source': market_data.source,
            'symbols_count': len(quotes)
        }
    })

@bp.route('/api/v1/integration/market/news')
def get_market_news():
    """Market news integration - standardized API contract"""
    news = market_data.get_news()
    return jsonify({
        'success': True,
        'data': news,
        'meta': {
            'timestamp': '2024-01-04T16:15:00Z',
            'source': market_data.source,
            'articles_count': len(news)
        }
    })

@bp.route('/api/v1/integration/broker/accounts')
def get_broker_accounts():
    """Broker integration interface - standardized API contract"""
    accounts = broker_api.get_accounts()
    return jsonify({
        'success': True,
        'data': accounts,
        'meta': {
            'timestamp': '2024-01-04T16:15:00Z',
            'broker': broker_api.broker_name,
            'accounts_count': len(accounts)
        }
    })

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'success': True,
        'data': {
            'pillar': 'ring',
            'status': 'healthy',
            'integrations_loaded': True
        }
    })