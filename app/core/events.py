from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict
import uuid

@dataclass
class GoldenHandEvent:
    event_id: str
    event_type: str
    source_pillar: str
    target_pillar: str
    timestamp: datetime
    payload: Dict[str, Any]
    metadata: Dict[str, Any]
    
    def __post_init__(self):
        if not self.event_id:
            self.event_id = str(uuid.uuid4())
        if not self.timestamp:
            self.timestamp = datetime.utcnow()

class EventBus:
    def __init__(self):
        self.subscribers = {}
    
    def publish(self, event: GoldenHandEvent):
        """Publish event to all subscribers"""
        print(f"📡 Event Published: {event.event_type} from {event.source_pillar} to {event.target_pillar}")
        for callback in self.subscribers.get(event.target_pillar, []):
            callback(event)
    
    def subscribe(self, pillar: str, callback):
        """Subscribe to events for a specific pillar"""
        if pillar not in self.subscribers:
            self.subscribers[pillar] = []
        self.subscribers[pillar].append(callback)
        print(f"📡 {pillar} pillar subscribed to events")

# Global event bus
event_bus = EventBus()