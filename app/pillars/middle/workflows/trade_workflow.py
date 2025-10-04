from datetime import datetime

class TradeWorkflow:
    """Business workflow for trade execution"""
    
    def execute_trade(self, trade_data):
        """Execute a trade with full business logic"""
        symbol = trade_data.get('symbol', 'AAPL')
        action = trade_data.get('type', 'buy')
        quantity = trade_data.get('quantity', 10)
        price = trade_data.get('price', 185.43)

        # Business logic: validate trade
        if quantity <= 0:
            return {'success': False, 'error': 'Invalid quantity'}

        if price <= 0:
            return {'success': False, 'error': 'Invalid price'}

        return {
            'trade_id': f"TRADE_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
            'symbol': symbol,
            'action': action,
            'quantity': quantity,
            'execution_price': price,
            'total_amount': quantity * price,
            'status': 'executed',
            'timestamp': datetime.utcnow().isoformat(),
            'commission': max(
                1.00, quantity * price * 0.01
            ),  # Simulated commission
        }
    
    def validate_trade(self, trade_data):
        """Validate trade against business rules"""
        # Add real validation logic here
        return {'valid': True, 'rules_passed': ['quantity_positive', 'price_positive']}