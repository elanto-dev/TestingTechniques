import socket
import constants
import apirequests as api
from requestsapi import login, create_room
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
        response, access_token = login(username,password)
        return response , access_token
        #response is of type request (!) so I just got the status code for 

def loginOutput(mess_in):

    response , access_token = processInput(mess_in)
    if response.status_code   == 200:
        mess_out = 'Response( OK, \"\")\n'
        token = access_token
        return mess_out

    elif response.status_code   == 403:
        mess_out = 'Response( Forbidden, \"\")\n'
        return mess_out


def roomCreateOutput(mess_in):
    logresponse , access_token = processInput(mess_in)
    roomresponse = create_room(access_token)
    if response.status_code   == 200:
        mess_out = 'Response( OK, \"\")\n'
        token = access_token
    elif response.status_code   == 403:
        mess_out = 'Response( Forbidden, \"\")\n'
    return mess_out
    

        
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

        message_out = loginOutput(mess_in)
        #or message_out = roomCreateOutput(mess_in)
        conn.send(message_out.encode())


        print(f'sent: {message_out}')