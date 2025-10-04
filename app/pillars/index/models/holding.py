from app import db
from datetime import datetime

class Holding(db.Model):
    __tablename__ = 'holdings'
    
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    average_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'portfolio_id': self.portfolio_id,
            'symbol': self.symbol,
            'quantity': self.quantity,
            'average_price': self.average_price,
            'total_cost': self.quantity * self.average_price,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }