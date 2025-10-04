from flask import Blueprint, jsonify, request
from .repositories.user_repository import UserRepository
from .repositories.portfolio_repository import PortfolioRepository
from .services.user_service import UserService
from .services.portfolio_service import PortfolioService

bp = Blueprint('index', __name__)

user_repo = UserRepository()
portfolio_repo = PortfolioRepository()
user_service = UserService()
portfolio_service = PortfolioService()

# Standardized Data API Endpoints
@bp.route('/api/v1/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user data - standardized API contract"""
    user = user_repo.get_by_id(user_id)
    if user:
        return jsonify({
            'success': True,
            'data': user.to_dict(),
            'meta': {
                'timestamp': '2024-01-04T12:00:00Z',  # Should be dynamic
                'endpoint': f'/api/v1/users/{user_id}'
            }
        })
    return jsonify({'success': False, 'error': 'User not found'}), 404

@bp.route('/api/v1/users/<int:user_id>/portfolios', methods=['GET'])
def get_user_portfolios(user_id):
    """Get user portfolios - standardized API contract"""
    portfolios = portfolio_repo.get_user_portfolios(user_id)
    return jsonify({
        'success': True,
        'data': [p.to_dict() for p in portfolios],
        'meta': {
            'timestamp': '2024-01-04T12:00:00Z',
            'user_id': user_id,
            'count': len(portfolios)
        }
    })

@bp.route('/api/v1/portfolios/<int:portfolio_id>', methods=['GET'])
def get_portfolio(portfolio_id):
    """Get portfolio data - standardized API contract"""
    portfolio = portfolio_repo.get_by_id(portfolio_id)
    if portfolio:
        return jsonify({
            'success': True,
            'data': portfolio.to_dict(),
            'meta': {
                'timestamp': '2024-01-04T12:00:00Z',
                'portfolio_id': portfolio_id
            }
        })
    return jsonify({'success': False, 'error': 'Portfolio not found'}), 404

@bp.route('/api/v1/portfolios', methods=['POST'])
def create_portfolio():
    """Create new portfolio - standardized API contract"""
    data = request.json
    portfolio = portfolio_repo.create(
        name=data.get('name'),
        user_id=data.get('user_id'),
        description=data.get('description')
    )
    
    return jsonify({
        'success': True,
        'data': portfolio.to_dict(),
        'meta': {
            'timestamp': '2024-01-04T12:00:00Z',
            'action': 'portfolio_created'
        }
    }), 201

# Health check for Index pillar
@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'success': True,
        'data': {
            'pillar': 'index',
            'status': 'healthy',
            'models_loaded': True
        }
    })