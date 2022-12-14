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
    return r,access_token

def create_room(access_token,name,preset,room_version,topic):
    command = "/createRoom"
    request_url = server_address + command
    headers = {"Authorization": "Bearer " + access_token}
    request_parameters = {
        "name": name,
        "preset": preset,
        "room_version": room_version,
        "topic": topic
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    print("successfully created a room")
    return r