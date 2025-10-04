from app.pillars.index.models.user import User
from app import db

class UserRepository:
    """Data access layer for User entities"""
    
    def get_by_id(self, user_id):
        return User.query.get(user_id)
    
    def get_by_username(self, username):
        return User.query.filter_by(username=username).first()
    
    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()
    
    def create(self, username, email, password, risk_tolerance='moderate', investment_goals=None):
        user = User(
            username=username,
            email=email,
            risk_tolerance=risk_tolerance,
            investment_goals=investment_goals
        )
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        return user
    
    def update_risk_profile(self, user_id, risk_tolerance, investment_goals):
        user = self.get_by_id(user_id)
        if user:
            user.risk_tolerance = risk_tolerance
            user.investment_goals = investment_goals
            db.session.commit()
        return user
    
    def get_all(self):
        return User.query.all()