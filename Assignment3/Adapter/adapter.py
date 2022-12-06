import socket

HOST = "localhost"
PORT = 8567

"""class ConnectionData:
    server_ip = constants.server_ip
    server_address = constants.server_ip
    access_token = ""

condata = ConnectionData"""

async def handler(data):
    print()

"""def processInput(self, message):
    if(message.startswith("ValidLogin")):
        return api.login(condata)
    if(message.startswith("InvalidLoginUser")):
        message.replace("InvalidLoginUser(", "")
        username = message[:-1]
        return api.login(condata, user=username)
    if(message.startswith("InvalidLoginPass")):
        message.replace("InvalidLoginPass(", "")
        password = message[:-1]"""
        
#condata.server_address = 'https://' + condata.server_ip + ':443/_matrix/client/v3'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        mess_in = data.decode()
        handler(mess_in)
        print(f'received: {mess_in}')
        mess_out = 'Response( Forbidden, \"\")\n'
        conn.send(mess_out.encode())
        print(f'sent: {mess_out}')