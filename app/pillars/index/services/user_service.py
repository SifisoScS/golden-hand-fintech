from app.pillars.index.repositories.user_repository import UserRepository

class UserService:
    """Business logic for user operations"""
    
    def __init__(self):
        self.user_repo = UserRepository()
    
    def create_user(self, username, email, password, risk_profile=None):
        # Validation logic
        if self.user_repo.get_by_username(username):
            raise ValueError("Username already exists")
        if self.user_repo.get_by_email(email):
            raise ValueError("Email already exists")
        
        return self.user_repo.create(username, email, password, risk_profile)
    
    def authenticate_user(self, username, password):
        user = self.user_repo.get_by_username(username)
        return user if user and user.check_password(password) else None
    
    def update_user_profile(self, user_id, risk_tolerance, investment_goals):
        return self.user_repo.update_risk_profile(user_id, risk_tolerance, investment_goals)
    
    def get_user_financial_profile(self, user_id):
        user = self.user_repo.get_by_id(user_id)
        if user:
            return {
                'risk_tolerance': user.risk_tolerance,
                'investment_goals': user.investment_goals,
                'portfolio_count': user.portfolios.count(),
                'total_transactions': user.transactions.count()
            }
        return None