from app.pillars.index.models.holding import Holding
from app import db

class HoldingRepository:
    """Data access layer for Holding entities"""
    
    def get_by_id(self, holding_id):
        return Holding.query.get(holding_id)
    
    def get_portfolio_holdings(self, portfolio_id):
        return Holding.query.filter_by(portfolio_id=portfolio_id).all()
    
    def create(self, portfolio_id, symbol, quantity, average_price):
        holding = Holding(
            portfolio_id=portfolio_id,
            symbol=symbol,
            quantity=quantity,
            average_price=average_price
        )
        db.session.add(holding)
        db.session.commit()
        return holding
    
    def update(self, holding_id, **kwargs):
        holding = self.get_by_id(holding_id)
        if holding:
            for key, value in kwargs.items():
                if hasattr(holding, key):
                    setattr(holding, key, value)
            db.session.commit()
        return holding
    
    def delete(self, holding_id):
        if holding := self.get_by_id(holding_id):
            db.session.delete(holding)
            db.session.commit()
            return True
        return False
    
    def get_by_symbol(self, portfolio_id, symbol):
        return Holding.query.filter_by(
            portfolio_id=portfolio_id, 
            symbol=symbol
        ).first()