from flask import Blueprint, request, jsonify
from app.core.events import event_bus, GoldenHandEvent
from .workflows.trade_workflow import TradeWorkflow
from .workflows.portfolio_workflow import PortfolioWorkflow

bp = Blueprint('middle', __name__)

trade_workflow = TradeWorkflow()
portfolio_workflow = PortfolioWorkflow()

@bp.route('/api/v1/process/trade', methods=['POST'])
def process_trade():
    """Trade execution workflow - standardized API contract"""
    trade_data = request.json
    
    # Create trade processing event
    event = GoldenHandEvent(
        event_type="trade.execution.requested",
        source_pillar="little",  # From user interface
        target_pillar="middle",  # To processing engine
        payload=trade_data,
        metadata={'user_id': 'demo_user'}  # TODO: Replace with actual user
    )
    
    # Process the trade through workflow
    result = trade_workflow.execute_trade(trade_data)
    
    # Publish result event for intelligence pillar
    result_event = GoldenHandEvent(
        event_type="trade.execution.completed", 
        source_pillar="middle",
        target_pillar="thumb",  # Send to intelligence for analysis
        payload=result,
        metadata={'user_id': 'demo_user'}
    )
    event_bus.publish(result_event)
    
    return jsonify({
        'success': True,
        'data': result,
        'meta': {
            'timestamp': '2024-01-04T16:15:00Z',
            'workflow': 'trade_execution',
            'status': 'completed'
        }
    })

@bp.route('/api/v1/process/portfolio/rebalance', methods=['POST'])
def rebalance_portfolio():
    """Portfolio rebalancing workflow - standardized API contract"""
    rebalance_data = request.json
    
    result = portfolio_workflow.rebalance_portfolio(rebalance_data)
    
    return jsonify({
        'success': True,
        'data': result,
        'meta': {
            'timestamp': '2024-01-04T16:15:00Z',
            'workflow': 'portfolio_rebalance',
            'status': 'completed'
        }
    })

@bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({
        'success': True,
        'data': {
            'pillar': 'middle',
            'status': 'healthy',
            'workflows_loaded': True
        }
    })