from app.pillars.index.models.transaction import Transaction
from app import db
from datetime import datetime, timedelta

class TransactionRepository:
    """Data access layer for Transaction entities"""
    
    def get_by_id(self, transaction_id):
        return Transaction.query.get(transaction_id)
    
    def get_user_transactions(self, user_id, limit=50):
        return Transaction.query.filter_by(user_id=user_id).order_by(
            Transaction.timestamp.desc()
        ).limit(limit).all()
    
    def get_portfolio_transactions(self, portfolio_id, limit=50):
        return Transaction.query.filter_by(portfolio_id=portfolio_id).order_by(
            Transaction.timestamp.desc()
        ).limit(limit).all()
    
    def create(self, user_id, portfolio_id, symbol, transaction_type, quantity, price, status='completed'):
        transaction = Transaction(
            user_id=user_id,
            portfolio_id=portfolio_id,
            symbol=symbol,
            transaction_type=transaction_type,
            quantity=quantity,
            price=price,
            status=status
        )
        db.session.add(transaction)
        db.session.commit()
        return transaction
    
    def get_recent_transactions(self, days=7):
        since_date = datetime.utcnow() - timedelta(days=days)
        return Transaction.query.filter(
            Transaction.timestamp >= since_date
        ).order_by(Transaction.timestamp.desc()).all()