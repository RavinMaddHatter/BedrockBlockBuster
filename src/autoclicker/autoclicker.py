import asyncio
import json
import uuid
import websockets
import pygetwindow as gw
import re
import time
import threading
import GuiNavigator as gn

commandPattern=r"Next Block: ([a-zA-Z:_]{1,}) ([a-zA-Z:_]{1,}-[a-zA-Z0-9]{1,} ){0,}"
permPattern=r"([a-zA-Z:_]{1,})-([a-zA-Z0-9]{1,} ){1,}"

lastRun =time.time()
def exportBlock(filename):
    gn.process_block(filename)
    time.sleep(0.1)
    lastRun =time.time()
    gn.next_block()
    
    
    
    
    
    
    
async def handle_connection(websocket):
    print("Minecraft connected!")
    
    # Subscribe to player chat messages (PlayerMessage event)
    subscribe_packet = {
        "header": {
            "version": 1,
            "requestId": str(uuid.uuid4()),
            "messageType": "commandRequest",
            "messagePurpose": "subscribe"
        },
        "body": {
            "eventName": "PlayerMessage"
        }
    }
    
    await websocket.send(json.dumps(subscribe_packet))
    print("Subscribed to chat events. Listening...")

    # Listen for incoming messages from Minecraft
    try:
        async for message in websocket:
            data = json.loads(message)
            header = data.get("header", {})
            body = data.get("body", {})
            
            if header.get("messagePurpose") == "event" and header.get("eventName") == "PlayerMessage":
                sender = body.get("sender")
                content = body.get("message")
                print(content)
                data =re.findall(commandPattern,content)
                print(data)
                if data:
                    data=data[0]
                    block = data [0]
                    block= block.replace("minecraft:","minecraft_")
                    permutations=[]
                    if len(data)>1:
                        for temp in data[1:]:
                            temp=temp.replace("minecraft:","minecraft_")
                            permutations.append(temp)
                    filename = block+" "+" ".join(permutations)
                    exportBlock(filename)
                    print(filename)
                        
                
    except websockets.exceptions.ConnectionClosed:
        print("Minecraft disconnected.")
        gn.reconnect()
        

async def main():
    # Start WebSocket server on localhost port 3000
    async with websockets.serve(handle_connection, "localhost", 3000):
        print("WebSocket server ready. In Minecraft chat, type: /connect localhost:3000")
        await asyncio.Future()  # Keep server running

if __name__ == "__main__":
    def run_loop():
        asyncio.run(main())
    thread = threading.Thread(target=run_loop, daemon=True)
    
    thread.start()
    time.sleep(1)
    clean=False
    if clean:
        gn.connect()
        gn.setup_pack()
        gn.next_block()
    else:
        gn.reconnect()

    

    
    
    
    
