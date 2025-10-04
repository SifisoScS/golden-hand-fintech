from flask import Blueprint, render_template, jsonify
from app.core.events import event_bus

bp = Blueprint('little', __name__)

# Our existing UI routes become features that consume pillar services
@bp.route('/')
def dashboard():
    """Main dashboard - consumes data from all pillars"""
    return render_template('dashboard.html')

@bp.route('/wealth-guide')
def wealth_guide():
    """Wealth guide feature - uses Intelligence + Data pillars"""
    return render_template('wealth_guide.html')

@bp.route('/vault-manager') 
def vault_manager():
    """Portfolio management - uses Data + Processing pillars"""
    return render_template('vault_manager.html')