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
    # login_manager.login_view = 'auth.login'  # Still commented out

    # Register all Golden Hand pillars
    pillars_loaded = []

    # True Golden Hand Architecture Pillars
    golden_pillars = [
        ('index', '/api/index'),
        ('middle', '/api/middle'), 
        ('ring', '/api/ring'),
        ('thumb', '/api/thumb'),
    ]

    for pillar_name, url_prefix in golden_pillars:
        try:
            module = __import__(f'app.pillars.{pillar_name}', fromlist=['bp'])
            bp = getattr(module, 'bp')
            app.register_blueprint(bp, url_prefix=url_prefix)
            pillars_loaded.append(pillar_name)
            print(f"✅ {pillar_name.upper()} Pillar loaded: {url_prefix}")
        except ImportError as e:
            print(f"❌ {pillar_name.upper()} Pillar failed: {e}")
        except AttributeError as e:
            print(f"❌ {pillar_name.upper()} Pillar missing blueprint: {e}")

    # Legacy feature pillars (User Interface - Little Pillar)
    legacy_pillars = [
        ('wealth_guide', '/wealth-guide'),
        ('vault_manager', '/vault-manager'),
        ('market_pulse', '/market-pulse'), 
        ('trade_nexus', '/trade-nexus'),
        ('insight_engine', '/insight-engine'),
        ('budget_tracker', '/budget-tracker'),
        ('crypto_wallet', '/crypto-wallet'),
        ('esg_analyzer', '/esg-analyzer'),
        ('community_forum', '/community-forum')
    ]

    for pillar_name, url_prefix in legacy_pillars:
        try:
            module = __import__(f'app.pillars.{pillar_name}', fromlist=['bp'])
            bp = getattr(module, 'bp')
            app.register_blueprint(bp, url_prefix=url_prefix)
            pillars_loaded.append(pillar_name)
            print(f"✅ {pillar_name} Feature loaded: {url_prefix}")
        except ImportError as e:
            print(f"❌ {pillar_name} Feature failed: {e}")

    print("🎯 GOLDEN HAND ARCHITECTURE READY")
    print(f"   Loaded pillars: {', '.join(pillars_loaded)}")

    # Setup intelligence event listeners
    try:
        from app.pillars.thumb import setup_intelligence_listeners
        setup_intelligence_listeners()
        print("🤖 Intelligence Hub event listeners activated")
    except ImportError as e:
        print(f"❌ Intelligence listeners failed: {e}")

    # Debug route to see all registered routes
    @app.route('/debug-routes')
    def debug_routes():
        routes = []
        for rule in app.url_map.iter_rules():
            if 'static' not in rule.endpoint:  # Skip static files
                routes.append({
                    'endpoint': rule.endpoint,
                    'methods': list(rule.methods),
                    'path': str(rule)
                })
        return {'routes': routes}

    # System status endpoint
    @app.route('/api/status')
    def system_status():
        return {
            'system': 'Golden Hand FinTech',
            'architecture': '5-Pillar Universal Framework',
            'status': 'operational',
            'timestamp': '2024-01-04T16:15:00Z',
            'pillars_loaded': pillars_loaded
        }

    @app.route('/')
    def index():
        return render_template('index.html')

    return app