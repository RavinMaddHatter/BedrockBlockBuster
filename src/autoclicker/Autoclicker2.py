from bedrock.server import Server
from bedrock.consts import NAME
from bedrock.context import PlayerMessageContext, ReadyContext
import time
import json
import structureNavigator as sn
import glob
import os
PREFIX = "#"
app = Server()
dumpFolder="D:\\test structura stuff\\dumps"
files = glob.glob(os.path.join(dumpFolder,'*.glb'))
finished = []
number =0
def incNumber():
    global number
    number+=1
    print(number)
for file_path in files:
    finished.append(os.path.splitext(os.path.basename(file_path))[0])

@app.game_event
async def player_message(ctx: PlayerMessageContext) -> None:
    global last, variables
    message = ctx.message
    
    if PREFIX in message:
        name = message.split("#")[1].replace("minecraft:","")
        #print(name)
        if not(name in finished or name =="skip"):
            sn.exportmcstructure(name)
            sn.export3d(name)
        #else:
        #    time.sleep(4/20)
        
        incNumber()
        await ctx.server.run("nextblock")
    else:
        print(message)
    

#minecraft:yellow_concrete_stairs upside_down_bit-false weirdo_direction-3 minecraft:corner-outer_right
app.start("localhost", 3000)
#mossy_stone_brick_stairs upside_down_bit-false weirdo_direction-2 corner-outer_left 
