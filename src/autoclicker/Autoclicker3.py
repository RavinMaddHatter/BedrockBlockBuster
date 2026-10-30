import asyncio
import json
import uuid
import websockets
import time
import structureNavigator as sn
PREFIX = "#"

async def handler(websocket):
    print("Minecraft client connected!")
    
    # Example command payload to send to Minecraft
    command_payload = {
        "header": {
            "version": "26.52",
            "requestId": str(uuid.uuid4()),
            "messageType": "commandRequest",
            "messagePurpose": "commandRequest"
        },
        "body": {
            "origin": {"type": "player"},
            "commandLine": "getblocks",
            "version": 1
        }
    }
    next_payload = {
        "header": {
            "version": "26.52",
            "requestId": str(uuid.uuid4()),
            "messageType": "commandRequest",
            "messagePurpose": "commandRequest"
        },
        "body": {
            "origin": {"type": "player"},
            "commandLine": "nextblock",
            "version": 1
        }
    }
    
    # Send the command
    #await websocket.send(json.dumps(command_payload))
    
    # Listen for responses/events from the game
    async for message in websocket:
        data = json.loads(message)
        print("Received from Minecraft:", json.dumps(data, indent=2))
        if "eventName" in data["header"].keys():
            if data["header"]["eventName"]=="PlayerMessage":
                if "#" in data["body"]["message"]:
                    print("next")
                    await websocket.send(json.dumps(next_payload))
                    
                elif "rawtext" in data["body"]["message"]:
                    message = json.loads(data["body"]["message"])


async def main():
    async with websockets.serve(handler, "localhost", 3000):
        print("WebSocket server running on ws://localhost:3000")
        print("In Minecraft chat, type: /connect localhost:3000")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
    
    

