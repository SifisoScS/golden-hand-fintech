from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
import sys

# Add the parent directory to Python path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config import Config
except ImportError:
    # Fallback config if config.py is missing
    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-change-in-production'
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'postgresql://goldenhand:password@db:5432/goldenhand'
        SQLALCHEMY_TRACK_MODIFICATIONS = False

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    
    # Register blueprints for each pillar
    try:
        from app.pillars.wealth_guide import bp as wealth_guide_bp
        from app.pillars.vault_manager import bp as vault_manager_bp
        from app.pillars.market_pulse import bp as market_pulse_bp
        from app.pillars.trade_nexus import bp as trade_nexus_bp
        from app.pillars.insight_engine import bp as insight_engine_bp
        
        app.register_blueprint(wealth_guide_bp, url_prefix='/wealth-guide')
        app.register_blueprint(vault_manager_bp, url_prefix='/vault-manager')
        app.register_blueprint(market_pulse_bp, url_prefix='/market-pulse')
        app.register_blueprint(trade_nexus_bp, url_prefix='/trade-nexus')
        app.register_blueprint(insight_engine_bp, url_prefix='/insight-engine')
    except ImportError as e:
        print(f"Warning: Some pillars not available - {e}")
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    return app