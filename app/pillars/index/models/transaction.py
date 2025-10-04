from app import db
from datetime import datetime

class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolios.id'), nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    transaction_type = db.Column(db.String(10), nullable=False)  # buy/sell
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='completed')  # pending, completed, cancelled
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Auto-calculate total amount
        if self.quantity and self.price and not self.total_amount:
            self.total_amount = self.quantity * self.price
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'portfolio_id': self.portfolio_id,
            'symbol': self.symbol,
            'transaction_type': self.transaction_type,
            'quantity': self.quantity,
            'price': self.price,
            'total_amount': self.total_amount,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
            'status': self.status
        }