import socket
import threading
from requestsapi import login, create_room
seperator = '@' #this will help getting username and password from torxakis very easily
host = "localhost"


def loginInput(userpass):
        fields = userpass.split(seperator)
        username = fields[0].strip() #Strip white spaces
        password = fields[1].strip() 
        response, access_token = login(username,password)
        return response , access_token

def loginOutput(mess_in):
    response , access_token = loginInput(mess_in)
    if response.status_code   == 200:
        mess_out = 'Response(OK)\n' 
        return mess_out
    elif response.status_code   == 403:
        mess_out = 'Response(Forbidden)\n'
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
        return 'Response(OK)\n' 
    elif response.status_code   == 401:
        return 'Response(Unauthorized)\n'
    return 'Should not be reached!'

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

def connection1():
    while True:
        print('we are using create room port')
        data = conn1.recv(1024)
        received = data.decode()
        print("Data received: ",  received )
        mess_out = roomCreateOutput(received)
        conn1.send(mess_out.encode())
        print("Data sent: ",  mess_out )

def connection2():
    while True:
        print('we are using login port')
        data = conn2.recv(1024)
        received = data.decode()
        print("Data received: ",  received )
        mess_out = loginOutput(received)
        conn2.send(mess_out.encode())
        print("Data sent: ",  mess_out )
        
x = threading.Thread(target=connection1)
x2 = threading.Thread(target=connection2)
x.start()
x2.start()





