from flask import Blueprint, render_template, jsonify

bp = Blueprint('wealth_guide', __name__)

@bp.route('/')
def dashboard():
    return render_template('wealth_guide_dashboard.html')

@bp.route('/recommendations')
def get_recommendations():
    # Use default risk profile since we don't have authentication yet
    risk_profile = 'moderate'  # Instead of current_user.risk_tolerance
    recommendations = generate_recommendations(risk_profile)
    return jsonify(recommendations)

def generate_recommendations(risk_profile):
    base_recommendations = {
        'conservative': [
            {'symbol': 'BND', 'allocation': 40, 'type': 'Bonds'},
            {'symbol': 'VTI', 'allocation': 30, 'type': 'Index Fund'},
            {'symbol': 'GLD', 'allocation': 20, 'type': 'Gold'},
            {'symbol': 'Cash', 'allocation': 10, 'type': 'Cash'}
        ],
        'moderate': [
            {'symbol': 'VTI', 'allocation': 50, 'type': 'Index Fund'},
            {'symbol': 'QQQ', 'allocation': 30, 'type': 'Tech ETF'},
            {'symbol': 'BND', 'allocation': 20, 'type': 'Bonds'}
        ],
        'aggressive': [
            {'symbol': 'QQQ', 'allocation': 40, 'type': 'Tech ETF'},
            {'symbol': 'ARKK', 'allocation': 30, 'type': 'Innovation ETF'},
            {'symbol': 'VTI', 'allocation': 20, 'type': 'Index Fund'},
            {'symbol': 'Individual Stocks', 'allocation': 10, 'type': 'High Growth'}
        ]
    }
    return base_recommendations.get(risk_profile, base_recommendations['moderate'])