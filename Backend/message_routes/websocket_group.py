from fastapi import WebSocket, WebSocketDisconnect, Depends
from .get_current_user import get_current_user
from typing import List,Dict

#we make it for a group chat also 
class GroupManager:
    def __init__(self):
        self.active_groups: Dict[str, List[WebSocket]] = {}
        
    async def connect(self, websocket: WebSocket, group_id: int):
        if group_id not in self.active_groups:
            self.active_groups[group_id] = []
        self.active_groups[group_id].append(websocket)
        await websocket.accept()
    
    async def disconnect(self,websocket: WebSocket, group_id: int):
        if group_id in self.active_groups:
            self.active_groups[group_id].remove(websocket)
            if not self.active_groups[group_id]:
                del self.active_groups[group_id]
    
    async def broadcast(self, message: str, group_id: int):
        if group_id in self.active_groups:
            for connection in self.active_groups[group_id]:
                await connection.send_text(message)

manager = GroupManager()

#now we make the endpoint
