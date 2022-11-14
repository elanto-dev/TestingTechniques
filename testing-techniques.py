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
    access_token = ""
    room_ids = []

    def setUp(self):
        self.server_address = 'https://' + self.server_ip + ':443/_matrix/client/v3'

    def tearDown(self):
        for room_id in self.room_ids:
            try:
                leave_room(self, room_id)
                forget_room(self, room_id)
            except:
                pass
        self.room_ids = []

    # def test_valid_login(self):
    #     r = login(self)
    #     response_data = r.json()
    #     self.assertIsNotNone(len(response_data["access_token"]), "access_token is missing from response")
    #     self.assertGreater(len(response_data["access_token"]), 0, "access_token's length should be greater than 0")
    #     self.assertTrue(r.ok)

    # def test_wrong_user(self):
    #     r = login(self, user="wrongusername")
    #     response_data = r.json()

    #     self.assertFalse(r.ok)
    #     self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
    #     self.assertEqual(response_data["error"], "Invalid username or password")

    # def test_wrong_password(self):
    #     r = login(self, password="wrongpassword")
    #     response_data = r.json()

    #     self.assertFalse(r.ok)
    #     self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
    #     self.assertEqual(response_data["error"], "Invalid username or password")

    def test_create_room(self):
        if not self.access_token:
            login(self)
        r = create_room(self)
        response_data = r.json()
        self.assertIsNotNone(len(response_data["room_id"]), "room_id is missing from response")
        self.assertTrue(r.ok)

    #     # state = get_state(self)   -produces error right now


    def test_leave_room(self):
        if not self.access_token:
            login(self)
        r = create_room(self)
        response_data = r.json()
        r = leave_room(self, response_data["room_id"])
        self.assertTrue(r.ok)

    def test_forget_room(self):
        if not self.access_token:
            login(self)
        r = create_room(self)
        response_data = r.json()
        leave_room(self, response_data["room_id"])
        r = forget_room(self, response_data["room_id"])
        self.assertTrue(r.ok)

    # def test_send_message(self):
        # if not self.access_token:
        #     login(self)
        # r = create_room(self)
        # response_data = r.json()
        # r = send_message(self, response_data["room_id"])
        # response_data = r.json()
        # print(response_data)
        # # self.assertIsNotNone(len(response_data["event_id"]), "event_id is missing from response")
        # self.assertTrue(r.ok)

    # def test_send_message_non_existing_room(self):
    #     if not self.access_token:
    #         login(self)
    #     r = send_message(self, "!VurgtrNIhiKZAYJtjX:testing-techniques")
    #     response_data = r.json()
    #     self.assertEqual(response_data["error"], "Unknown room")
    #     self.assertTrue(r.ok)



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
        pass

    return r

# returns room id as string


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

    try:
        context.room_ids.append(r.json()["room_id"])
    except:
        pass

    return r

# leaves room returns nothing (check with get_state)


def leave_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/leave"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r

# forgets room returns nothing (check with get_state)


def forget_room(context, room_id):
    command = "/rooms/" + str(room_id) + "/forget"
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    try:
        context.room_ids.remove(r.json()["room_id"])
    except:
        pass

    return r

# returns the message event id


def send_message(context, room_id):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {
        "body": "hello this is a test message :D\n",
        "msgtype": "m.text",
        "type": "m.room.message",
        "sender": "@matrixadmin:testing-techniques"
    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)

    return r


# edits message returns nothing (check with get_state)
def edit_message(context, room_id, message_id):
    command = "/rooms/" + str(room_id) + \
        "/send/m.room.message/" + str(random.random())
    request_url = context.server_address + command
    headers = {"Authorization": "Bearer " + context.access_token}
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
    headers = {"Authorization": "Bearer " + context.access_token}
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
    headers = {"Authorization": "Bearer " + context.access_token}
    request_parameters = {

    }
    r = requests.post(url=request_url, headers=headers, data=json.dumps(
        request_parameters), verify=False)
    response_data = r.json()
    context.assertTrue(r.ok)
    return response_data


if __name__ == '__main__':
    unittest.main()
