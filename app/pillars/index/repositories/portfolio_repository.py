from app.pillars.index.models.portfolio import Portfolio
from app.pillars.index.models.holding import Holding
from app import db

class PortfolioRepository:
    """Data access layer for Portfolio entities"""
    
    def get_by_id(self, portfolio_id):
        return Portfolio.query.get(portfolio_id)
    
    def get_user_portfolios(self, user_id):
        return Portfolio.query.filter_by(user_id=user_id).all()
    
    def create(self, name, user_id, description=None):
        portfolio = Portfolio(
            name=name,
            user_id=user_id,
            description=description
        )
        return self._extracted_from_add_holding_7(portfolio)
    
    def update(self, portfolio_id, **kwargs):
        portfolio = self.get_by_id(portfolio_id)
        if portfolio:
            for key, value in kwargs.items():
                if hasattr(portfolio, key):
                    setattr(portfolio, key, value)
            db.session.commit()
        return portfolio
    
    def delete(self, portfolio_id):
        if portfolio := self.get_by_id(portfolio_id):
            db.session.delete(portfolio)
            db.session.commit()
            return True
        return False
    
    def add_holding(self, portfolio_id, symbol, quantity, average_price):
        if portfolio := self.get_by_id(portfolio_id):
            holding = Holding(
                portfolio_id=portfolio_id,
                symbol=symbol,
                quantity=quantity,
                average_price=average_price
            )
            return self._extracted_from_add_holding_7(holding)
        return None

    # TODO Rename this here and in `create` and `add_holding`
    def _extracted_from_add_holding_7(self, arg0):
        db.session.add(arg0)
        db.session.commit()
        return arg0