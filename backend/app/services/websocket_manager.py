import json
from typing import List, Dict, Any
from fastapi import WebSocket
from core.logger import logger

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
        logger.info(f"WebSocket client connected. Total clients: {len(self.active_connections)}")

    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            logger.info(f"WebSocket client disconnected. Total clients: {len(self.active_connections)}")

    async def broadcast(self, event_type: str, payload: Dict[str, Any]):
        """
        Broadcasts a structured event to all connected clients.
        Format:
        {
            "event": "NEW_READING",
            "payload": { ... }
        }
        """
        message = {
            "event": event_type,
            "payload": payload
        }
        
        # We need to copy the list in case clients disconnect during broadcast
        for connection in list(self.active_connections):
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Error broadcasting to client: {e}")
                self.disconnect(connection)

manager = ConnectionManager()
