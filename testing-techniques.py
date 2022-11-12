from distutils.cmd import Command
import json
import unittest
import requests
import constants
import random


class MatrixTestingClass(unittest.TestCase):
    # will run any function where the name starts with test_
    server_ip = constants.server_ip
    server_address = constants.server_ip
    acsess_token = ""

    def setUp(self):
        self.server_address = 'https://' + self.server_ip + ':443/_matrix/client/v3'

    def test_valid_login(self):
        login(self)


# individual functions to make chaining easy
# context is the passed self in MatrixTestingClass so we can access it's internal variables

# returns the accsess token
def login(context):
    command = "/login"
    request_url = context.server_address + command
    request_parameters = {
        "identifier": {
            "type": "m.id.user",
            "user": "matrixadmin"
        },
        "initial_device_display_name": "Jungle Phone",
        "password": "admin", "type": "m.login.password"
    }
    r = requests.post(url=request_url, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertIsNotNone(
        len(response_data["access_token"]), "access_token is missing from response")
    context.assertGreater(len(
        response_data["access_token"]), 0, "access_token's length should be greater than 0")
    context.acsess_token = response_data["access_token"]
    context.assertTrue(r.ok)
    return response_data["access_token"]

# returns room id as string
def create_room(context):
    command = "/createRoom"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
        "name": "the big test room",
        "preset": "public_chat",
        "room_version": "1",
        "topic": "All about not existing for very long."
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertIsNotNone(
        len(response_data["room_id"]), "room_id is missing from response")
    context.assertTrue(r.ok)
    return response_data["room_id"]

# leaves room returns nothing (check with get_state)
def leave_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/leave"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    context.assertTrue(r.ok)
    return

# forgets room returns nothing (check with get_state)
def forget_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/forget"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    context.assertTrue(r.ok)
    return

# returns the message event id
def send_message(context, room_id):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
        "body": "hello this is a test message :D\n",
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques"
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertIsNotNone(
        len(response_data["send_message_event_id"]), "send_message_event_id is missing from response")
    context.assertTrue(r.ok)
    return response_data["send_message_event_id"]


# edits message returns nothing (check with get_state)
def edit_message(context, room_id, message_id):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
        "body": "i have been \nedited \na \nlot",
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
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertTrue(r.ok)
    return

# redact message returns nothing (check with get_state)
def redact_message(context, room_id, message_id):
    command = "/rooms/" + str(room_id) + "/redact/" + \
        str(message_id) + "/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {
        "body": "hello this is a test message :D\n",
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques"
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertTrue(r.ok)
    return


# retrieves all information needed to populate the gui. should be used to check room creation deletion etc.
# returns all the json. (as dict)
def get_state(context):
    command = "/sync"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.acsess_token}
    request_parameters = {

    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertTrue(r.ok)
    return response_data


if __name__ == '__main__':
    unittest.main()
