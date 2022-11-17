import json
import random

import requests

# individual functions to make chaining easy
# context is the passed self in MatrixTestingClass so we can access it's internal variables

# returns the response


def login(context, user="matrixadmin", password="admin"):
    command = "/login"
    request_url = context.server_address + command
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
        context.access_token = r.json()["access_token"]
    except:
        context.access_token = ""

    return r

# creates room


def create_room(context):
    command = "/createRoom"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
        "name": "the big test room",
        "preset": "public_chat",
        "room_version": "1",
        "topic": "All about not existing for very long."
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r

# leaves room


def leave_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/leave"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r

# forgets room


def forget_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/forget"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r

# send a message


def send_message(context, room_id, message="hello this is a test message :D\n"):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
        "body": message,
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques"
    }
    r = requests.put(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r


# edits message


def edit_message(context, room_id, message_id, new_message="i have been \nedited \na \nlot"):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
        "body": new_message,
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques",
        "m.new_content": {
            "org.matrix.msc1767.text": "i have been \nedited \na \nlot",
            "body": "i have been \nedited \na \nlot",
            "msgtype": "m.text"},
        "m.relates_to": {
            "rel_type": "m.replace",
            "event_id": str(message_id)}
    }
    r = requests.put(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r

# redact message


def redact_message(context, room_id, message_id):
    command = "/rooms/" + str(room_id) + "/redact/" + \
        str(message_id) + "/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
        "body": "hello this is a test message :D\n",
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques"
    }
    r = requests.put(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r


# retrieves all information needed to populate the gui. should be used to check room creation deletion etc.
# returns all the json. (as dict)
def get_state(context):
    command = "/sync"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {

    }
    r = requests.get(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    return response_data

