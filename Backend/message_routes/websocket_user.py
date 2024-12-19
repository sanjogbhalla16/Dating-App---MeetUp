from fastapi import WebSocket, WebSocketDisconnect, Depends
from .get_current_user import get_current_user
from typing import List,Dict

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

#now we will make the websocket connection
router.webscoket()
async def websocket_endpoint(websocket: WebSocket, current_user = Depends(get_current_user)):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{current_user.email}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        
        
        
