import socket
import constants
import apirequests as api
from requestsapi import login, create_room
seperator = '@' #this will help getting username and password from torxakis very easily
host = "localhost"

class ConnectionData:
    server_ip = constants.server_ip
    server_address = constants.server_ip
    access_token = ""

condata = ConnectionData


def loginInput(userpass):
        fields = userpass.split(seperator)
        username = fields[0].strip() #Strip white spaces
        password = fields[1].strip() 
        response, access_token = login(username,password)
        return response , access_token

def loginOutput(mess_in):
    response , access_token = loginInput(mess_in)
    if response.status_code   == 200:
        mess_out = 'ResponseCode(OK)\n' 
        return mess_out
    elif response.status_code   == 403:
        mess_out = 'ResponseCode(Forbidden)\n'
        return mess_out



def roomCreateInput(mess_in):
        fields = mess_in.split(seperator)
        name = fields[0].strip() #Strip white spaces
        topic = fields[1].strip() 
        preset = fields[2].strip() 
        version = fields[3].strip() 
        accesstokenmodel = fields[4].strip() 
        
        if accesstokenmodel == "correcttoken":
            logresponse, access_token = login("matrixadmin","admin")
            crresponse = create_room(access_token,name,preset,version,topic)
        else:
            crresponse = create_room(accesstokenmodel,name,preset,version,topic)
        return crresponse
        
def roomCreateOutput(mess_in):
    response = roomCreateInput(mess_in)
    if response.status_code   == 200:
        mess_out = 'ResponseCode(OK)\n' 
    elif response.status_code   == 403:
        mess_out = 'ResponseCode(Forbidden)\n'
    return mess_out
    

        
condata = ConnectionData()
condata.server_address = 'https://' + condata.server_ip + ':443/_matrix/client/v3'

# create a socket object
s1 = socket.socket()
s2 = socket.socket()

# specify the ports that each socket should listen on
ports = [8567, 8568]

# bind each socket to its corresponding port
s1.bind((host, ports[0]))
s2.bind((host, ports[1]))

# start listening for incoming connections on each socket
s1.listen(2)
s2.listen(2)

# accept incoming connections on each socket
conn1, addr1 = s1.accept()
conn2, addr2 = s2.accept()

print(f'Connected by {addr1} and {addr2}')

while True:
    if conn1:
        print('we are using create room port')
        data = conn1.recv(1024)
        received = data.decode()
        print("Data received: ",  received )
        mess_out = roomCreateOutput(received)
        conn1.send(mess_out.encode())
        print("Data sent: ",  mess_out )

    elif conn2:
        print('we are using login port')






