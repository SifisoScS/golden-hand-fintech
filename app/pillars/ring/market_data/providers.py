import random
from datetime import datetime

class MarketDataProvider:
    """Unified market data provider (simulates real API)"""
    
    def __init__(self):
        self.source = "Golden Hand Market Data"
        self.base_prices = {
            'AAPL': 185.43, 'MSFT': 374.58, 'GOOGL': 138.21, 
            'VTI': 234.56, 'QQQ': 389.12, 'ARKK': 45.67,
            'TSLA': 245.78, 'NVDA': 465.32, 'BND': 78.90
        }
    
    def get_quotes(self, symbols):
        """Get real-time quotes for symbols"""
        quotes = {}
        for symbol in symbols:
            base_price = self.base_prices.get(symbol.upper(), 100.00)
            # Simulate price movement
            change_percent = random.uniform(-2.0, 2.0)
            change = base_price * (change_percent / 100)
            current_price = base_price + change
            
            quotes[symbol.upper()] = {
                'price': round(current_price, 2),
                'change': round(change, 2),
                'changePercent': round(change_percent, 2),
                'volume': random.randint(1000000, 50000000),
                'timestamp': datetime.utcnow().isoformat()
            }
        return quotes
    
    def get_news(self):
        """Get market news"""
        return [
            {
                'title': 'Tech Stocks Rally on AI Optimism',
                'source': 'Financial Times',
                'timestamp': datetime.utcnow().isoformat(),
                'sentiment': 'positive'
            },
            {
                'title': 'Federal Reserve Holds Rates Steady',
                'source': 'Bloomberg',
                'timestamp': datetime.utcnow().isoformat(),
                'sentiment': 'neutral'
            }
        ]