import json
import random
import requests
import constants

# a copy of apirequests because i'm modifying it and i wanna have a backup  
server_address = 'https://' + constants.server_ip + ':443/_matrix/client/v3'

def login(user, password):
    command = "/login"
    request_url = server_address + command
    request_parameters = {
        "identifier": {
            "type": "m.id.user",
            "user": user
        },
        "initial_device_display_name": "Jungle Phone",
        "password": password, "type": "m.login.password"
    }
    r = requests.post(url=request_url, data=json.dumps(
        request_parameters), verify=False)

    try:
        access_token = r.json()["access_token"]
    except:
        access_token = ""
    # print(access_token)
    return r,access_token

def create_room(access_token):
    command = "/createRoom"
    request_url = server_address + command
    headers = {"Authorization": "Bearer " + access_token}
    request_parameters = {
        "name": "torxakis support group",
        "preset": "public_chat",
        "room_version": "1",
        "topic": "All about not existing for very long."
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    print("successfully created a room")
    return r

# response , token = login(user,password)
# create_room(token)
# print("room created")



