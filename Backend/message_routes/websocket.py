from fastapi import WebSocket, WebSocketDisconnect, Depends
from .get_current_user import get_current_user
from typing import List

#now we first make the class for the websocket
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
        
    async def send_personal_message(self, message:str,websocket: WebSocket):
        await websocket.send_text(message)
        
    async def broadcast(self, message:str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()
        