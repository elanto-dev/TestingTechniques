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

    def setUp(self):
        self.server_address = 'https://' + self.server_ip + ':443/_matrix/client/v3'  # r0

    def tearDown(self):
        r = get_state(self)
        if "rooms" in r:
            for room_id in r["rooms"]["join"]:
                try:
                    leave_room(self, room_id)
                except:
                    print("leave failed for " + room_id)
                try:
                    forget_room(self, room_id)
                except:
                    print("forget failed for " + room_id)

    # TestCase 1
    def test_create_room_not_logged_in(self):
        r = login(self, password="wrongpassword")
        r = create_room(self)
        response_data = r.json()
        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_MISSING_TOKEN")
        self.assertEqual(response_data["error"], "Invalid Authorization header.")    

    # TestCase 2
    def test_wrong_user(self):
        r = login(self, user="wrongusername")
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertEqual(response_data["error"], "Invalid username or password")

    # TestCase 3
    def test_wrong_password(self):
        r = login(self, password="wrongpassword")
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertEqual(response_data["error"], "Invalid username or password")

    # TestCase 4
    def test_valid_login(self):
        r = login(self)
        response_data = r.json()

        self.assertIsNotNone(len(response_data["access_token"]), "access_token is missing from response")
        self.assertGreater(len(response_data["access_token"]), 0, "access_token's length should be greater than 0")
        self.assertTrue(r.ok)

    # TestCase 5
    def test_send_message_non_existing_room(self):
        login(self)
        r = send_message(self, "!VurgtrNIhiKZAYJtjX:testing-techniques")
        response_data = r.json()
        self.assertEqual(response_data["error"], "Unknown room")
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertFalse(r.ok)

    # TestCase 6
    def test_create_room(self):
        login(self)
        r = create_room(self)
        response_data = r.json()
        self.assertIsNotNone(len(response_data["room_id"]), "room_id is missing from response")
        self.assertTrue(r.ok)

        state = get_state(self)
        self.assertIsNotNone(state["rooms"]["join"][response_data["room_id"]])

    # TestCase 7
    def test_send_message(self):
        message = "hello this is a test message :D\n"

        login(self)
        r = create_room(self)
        room_id = r.json()["room_id"]

        r = send_message(self, room_id, message)
        event_id = r.json()["event_id"]

        self.assertIsNotNone(
            len(event_id), "event_id is missing from response")
        self.assertTrue(r.ok)

        state = get_state(self)
        message_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == event_id and event["content"]["body"] == message:
                message_found = True
                break
        self.assertTrue(message_found)    

    # TestCase 8
    def test_edit_message(self):
        new_message = "i have been \nedited \na \nlot"
        login(self)
        r = create_room(self)
        room_id = r.json()["room_id"]

        r = send_message(self, room_id)
        event_id_send = r.json()["event_id"]

        r = edit_message(self, room_id, event_id_send, new_message)
        event_id_edit = r.json()["event_id"]

        self.assertIsNotNone(
            len(r.json()["event_id"]), "event_id is missing from response")
        self.assertTrue(r.ok)

        state = get_state(self)
        edit_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == event_id_edit and event["content"]["body"] == new_message:
                edit_found = True
                break
        self.assertTrue(edit_found)

    # TestCase 9
    def test_redact_message(self):
        login(self)
        r = create_room(self)
        room_id = r.json()["room_id"]

        r = send_message(self, room_id)
        event_id_send = r.json()["event_id"]

        r = redact_message(self, room_id, event_id_send)
        event_id_redact = r.json()["event_id"]

        self.assertIsNotNone(len(event_id_redact),
                             "event_id is missing from response")
        self.assertTrue(r.ok)

        state = get_state(self)
        redact_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.redaction" and event["event_id"] == event_id_redact:
                redact_found = True
                break
        self.assertTrue(redact_found)

    # TestCase 10
    def test_forget_room(self):
        login(self)
        r = create_room(self)
        response_data = r.json()
        leave_room(self, response_data["room_id"])
        r = forget_room(self, response_data["room_id"])
        self.assertTrue(r.ok)

    # TestCase 11
    def test_leave_room(self):
        login(self)
        r = create_room(self)
        response_data = r.json()
        r = leave_room(self, response_data["room_id"])
        self.assertTrue(r.ok)

        state = get_state(self)
        self.assertRaises(
            KeyError, lambda: state["rooms"]["join"][response_data["room_id"]])

    # TestCase 12
    def test_edit_message_after_leaving_room(self):
        new_message = "i have been \nedited \na \nlot"
        login(self)
        r = create_room(self)
        room_id = r.json()["room_id"]

        r = send_message(self, room_id)
        event_id_send = r.json()["event_id"]

        leave_room(self, room_id)

        r = edit_message(self, room_id, event_id_send, new_message)
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertTrue(response_data["error"].__contains__("not in room " + room_id))

    

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


if __name__ == '__main__':
    unittest.main()
