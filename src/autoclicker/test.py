import json
data = {}
with open("dumpedLogs.txt","r+") as file:
    for line in file:
        content =line.split("[inform]-")[-1]
        try:
            data.update(json.loads(content))
        except:
            pass
with open("blocks.json","w+" ) as file:
    json.dump(data,file,indent=4)
