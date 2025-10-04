from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Portfolio, Holding, db

bp = Blueprint('vault_manager', __name__)

@bp.route('/')
@login_required
def portfolio_overview():
    portfolios = current_user.portfolios.all()
    return render_template('vault_manager/overview.html', portfolios=portfolios)

@bp.route('/portfolio/<int:portfolio_id>')
@login_required
def portfolio_detail(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    if portfolio.owner != current_user:
        return "Unauthorized", 403
    
    holdings = portfolio.holdings.all()
    return render_template('vault_manager/detail.html', portfolio=portfolio, holdings=holdings)

@bp.route('/create-portfolio', methods=['POST'])
@login_required
def create_portfolio():
    name = request.json.get('name')
    portfolio = Portfolio(name=name, owner=current_user)
    db.session.add(portfolio)
    db.session.commit()
    return jsonify({'success': True, 'portfolio_id': portfolio.id})