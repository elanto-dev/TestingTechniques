import socket
import constants
import apirequests as api

HOST = "localhost"
PORT = 8567

class ConnectionData:
    server_ip = constants.server_ip
    server_address = constants.server_ip
    access_token = ""

condata = ConnectionData

def handler(data):
    data = processInput(data)
    return data

def processInput(message):
    if(message.startswith("ValidLogin")):
        return ""
    if(message.startswith("InvalidUsernameLogin")):
        message.replace("InvalidUsernameLogin(", "")
        username = message[:-1]
        return 'Response( Forbidden, \"\")\n'
    if(message.startswith("InvalidPasswordLogin")):
        message.replace("InvalidPasswordLogin(", "")
        password = message[:-1]
        return 'Response( Forbidden, \"\")\n'
        
condata = ConnectionData()
condata.server_address = 'https://' + condata.server_ip + ':443/_matrix/client/v3'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    print(f'Connected by {addr}')
    while True:
        data = conn.recv(1024)
        mess_in = data.decode()
        print(f'received: {mess_in}')
        mess_out = 'Response( Forbidden, \"\")\n'
        conn.send(mess_out.encode())
        print(f'sent: {mess_out}')