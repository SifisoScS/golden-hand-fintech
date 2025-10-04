from flask import Blueprint, render_template, jsonify, request
# from flask_login import login_required, current_user  # COMMENT OUT
from app.models import Portfolio, Holding, db

bp = Blueprint('vault_manager', __name__)

@bp.route('/')
# @login_required  # COMMENT OUT
def portfolio_overview():
    # TEMPORARY: Return demo data instead of user portfolios
    # portfolios = current_user.portfolios.all()
    demo_portfolios = [
        {'id': 1, 'name': 'Growth Portfolio', 'value': 45230.15},
        {'id': 2, 'name': 'Retirement Fund', 'value': 125000.00},
        {'id': 3, 'name': 'Emergency Fund', 'value': 15000.00}
    ]
    return render_template('vault_manager_dashboard.html', portfolios=demo_portfolios)

@bp.route('/portfolio/<int:portfolio_id>')
# @login_required  # COMMENT OUT
def portfolio_detail(portfolio_id):
    # TEMPORARY: Demo holdings data
    # portfolio = Portfolio.query.get_or_404(portfolio_id)
    # if portfolio.owner != current_user:
    #     return "Unauthorized", 403
    
    demo_holdings = [
        {'symbol': 'AAPL', 'quantity': 10, 'average_price': 150.00, 'current_price': 185.43},
        {'symbol': 'MSFT', 'quantity': 5, 'average_price': 300.00, 'current_price': 374.58},
        {'symbol': 'VTI', 'quantity': 25, 'average_price': 220.00, 'current_price': 234.56}
    ]
    
    demo_portfolio = {'id': portfolio_id, 'name': 'Demo Portfolio'}
    return render_template('vault_manager_detail.html', portfolio=demo_portfolio, holdings=demo_holdings)

@bp.route('/create-portfolio', methods=['POST'])
# @login_required  # COMMENT OUT
def create_portfolio():
    name = request.json.get('name')
    # TEMPORARY: Just return success without saving to DB
    # portfolio = Portfolio(name=name, owner=current_user)
    # db.session.add(portfolio)
    # db.session.commit()
    return jsonify({'success': True, 'portfolio_id': 999, 'message': 'Demo mode - portfolio not saved'})