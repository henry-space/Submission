# -*- coding: utf-8 -*-


from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List

app = FastAPI()




class ConnectionManager:
    
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
        
            
manager = ConnectionManager()



@app.websocket("/ws/{username}")          
async def websocket_endpoint(websocket: WebSocket, username: str):
    
    await manager.connect(websocket)
    await manager.broadcast(f"{username}")
    
    try:
        while True:
            msg = await websocket.receive_text()
            await manager.broadcast(f"{username}: {msg}")
            
    except WebSocketDisconnect:
        manager.disconnect(websocket)
