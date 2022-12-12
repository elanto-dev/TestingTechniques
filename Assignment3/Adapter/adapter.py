import socket
import constants
import apirequests as api
from login import login
seperator = '@' #this will help getting username and password from torxakis very easily
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

def processInput(userpass):
        fields = userpass.split(seperator)
        username = fields[0].strip() #Strip white spaces
        password = fields[1].strip() 
        response = login(username,password)
        return response.status_code  #response is of type request (!) so I just got the status code for 


        
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
        
        responsecode = processInput(mess_in)

        if responsecode == 200:
            mess_out = 'Response( OK, \"\")\n'
        elif responsecode == 403:
            mess_out = 'Response( Forbidden, \"\")\n'
        conn.send(mess_out.encode())
        print(f'sent: {mess_out}')