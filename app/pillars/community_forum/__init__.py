from flask import Blueprint, render_template, jsonify, request
from datetime import datetime, timedelta
import random

bp = Blueprint('community_forum', __name__)

class CommunityAgent:
    """Community engagement agent with gamification"""
    
    def __init__(self):
        self.discussions = self.generate_sample_discussions()
        self.leaderboard = self.generate_leaderboard()
    
    def generate_sample_discussions(self):
        """Generate sample discussion data"""
        topics = [
            "Investment Strategies in Volatile Markets",
            "ESG Investing Best Practices", 
            "Cryptocurrency Portfolio Allocation",
            "Retirement Planning Tips",
            "AI in Personal Finance"
        ]

        discussions = []
        discussions.extend(
            {
                'id': i + 1,
                'topic': topic,
                'author': f"User{random.randint(1000, 9999)}",
                'replies': random.randint(5, 50),
                'views': random.randint(100, 1000),
                'last_activity': (
                    datetime.now() - timedelta(hours=random.randint(1, 24))
                ).isoformat(),
                'engagement_score': random.randint(70, 95),
            }
            for i, topic in enumerate(topics)
        )
        return discussions
    
    def generate_leaderboard(self):
        """Generate gamification leaderboard"""
        users = []
        users.extend(
            {
                'rank': i + 1,
                'username': f"FinTechExpert{i+1}",
                'points': random.randint(1000, 5000),
                'badges': random.randint(3, 15),
                'contribution_level': ['Novice', 'Contributor', 'Expert', 'Guru'][
                    min(i // 3, 3)
                ],
            }
            for i in range(10)
        )
        return users
    
    def get_trending_topics(self):
        """Get trending discussion topics"""
        return sorted(self.discussions, key=lambda x: x['engagement_score'], reverse=True)[:3]

community_agent = CommunityAgent()

@bp.route('/')
def forum_dashboard():
    """Community forum main dashboard"""
    return render_template('community_forum_dashboard.html')

@bp.route('/api/discussions')
def get_discussions():
    """Get community discussions"""
    return jsonify({
        'success': True,
        'data': community_agent.discussions,
        'meta': {
            'total_discussions': len(community_agent.discussions),
            'active_users': random.randint(50, 200)
        }
    })

@bp.route('/api/leaderboard')
def get_leaderboard():
    """Get community leaderboard"""
    return jsonify({
        'success': True,
        'data': community_agent.leaderboard,
        'meta': {
            'season': 'Q1 2025',
            'reset_date': (datetime.now() + timedelta(days=30)).isoformat()
        }
    })