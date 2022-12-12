import json
import random
import requests
import constants

# A simple login without context (yet) because I was confused about making it work with the ones in apitests! 

def login(user, password):
    command = "/login"
    server_address = 'https://' + constants.server_ip + ':443/_matrix/client/v3'
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
    print("Logged in Successfully!")
    return r




