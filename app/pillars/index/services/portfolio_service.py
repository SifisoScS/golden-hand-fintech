from app.pillars.index.repositories.portfolio_repository import PortfolioRepository
from app.pillars.index.repositories.holding_repository import HoldingRepository

class PortfolioService:
    """Business logic for portfolio operations"""
    
    def __init__(self):
        self.portfolio_repo = PortfolioRepository()
        self.holding_repo = HoldingRepository()
    
    def create_user_portfolio(self, user_id, name, description=None):
        return self.portfolio_repo.create(name, user_id, description)
    
    def get_portfolio_summary(self, portfolio_id):
        if portfolio := self.portfolio_repo.get_by_id(portfolio_id):
            holdings = portfolio.holdings.all()
            total_value = sum(h.quantity * h.average_price for h in holdings)

            return {
                'portfolio': portfolio.to_dict(),
                'holdings_count': len(holdings),
                'total_value': total_value,
                'holdings': [h.to_dict() for h in holdings]
            }
        return None
    
    def get_user_portfolios_summary(self, user_id):
        portfolios = self.portfolio_repo.get_user_portfolios(user_id)
        summary = []
        
        for portfolio in portfolios:
            holdings = portfolio.holdings.all()
            total_value = sum(h.quantity * h.average_price for h in holdings)
            
            summary.append({
                'portfolio': portfolio.to_dict(),
                'total_value': total_value,
                'holdings_count': len(holdings)
            })
        
        return summary