import asyncio
import constants
import websockets

class ConnectionData:
    server_ip = constants.server_ip
    server_address = constants.server_ip
    access_token = ""

condata = ConnectionData

async def handler(websocket, path):
    data = await websocket.recv()
    print(data)
    await websocket.send("Response( Forbidden, "" )")

"""def processInput(self, message):
    if(message.startswith("ValidLogin")):
        return api.login(condata)
    if(message.startswith("InvalidLoginUser")):
        message.replace("InvalidLoginUser(", "")
        username = message[:-1]
        return api.login(condata, user=username)
    if(message.startswith("InvalidLoginPass")):
        message.replace("InvalidLoginPass(", "")
        password = message[:-1]
        return api.login(self.condata, password=password)
        """
        


#condata.server_address = 'https://' + condata.server_ip + ':443/_matrix/client/v3'
start_server = websockets.serve(handler, "localhost", 8567)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()