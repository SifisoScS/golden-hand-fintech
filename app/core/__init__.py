# Core shared interfaces for Golden Hand architecture
from .events import event_bus, GoldenHandEvent
from .auth import login_manager, GoldenHandUserContext

__all__ = ['event_bus', 'GoldenHandEvent', 'login_manager', 'GoldenHandUserContext']