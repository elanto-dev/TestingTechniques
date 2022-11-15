from distutils.cmd import Command
import json
import unittest
import requests
import constants
import apirequests as api


class MatrixTestingClass(unittest.TestCase):
    # will run any function where the name starts with test_

    class ConnectionData:
            server_ip = constants.server_ip
            server_address = constants.server_ip
            access_token = ""

    condata = ConnectionData

    def setUp(self):
        self.condata.server_address = 'https://' + self.condata.server_ip + ':443/_matrix/client/v3'

    def tearDown(self):
        r = api.get_state(self.condata)
        if "rooms" in r:
            for room_id in r["rooms"]["join"]:
                try:
                    api.leave_room(self.condata, room_id)
                except:
                    print("leave failed for " + room_id)
                try:
                    api.forget_room(self.condata, room_id)
                except:
                    print("forget failed for " + room_id)

    # TestCase 1
    def test_create_room_not_logged_in(self):
        r = api.login(self.condata, password="wrongpassword")
        r = api.create_room(self.condata)
        response_data = r.json()
        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_MISSING_TOKEN")
        self.assertEqual(response_data["error"], "Invalid Authorization header.")    

    # TestCase 2
    def test_wrong_user(self):
        r = api.login(self.condata, user="wrongusername")
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertEqual(response_data["error"], "Invalid username or password")

    # TestCase 3
    def test_wrong_password(self):
        r = api.login(self.condata, password="wrongpassword")
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertEqual(response_data["error"], "Invalid username or password")

    # TestCase 4
    def test_valid_login(self):
        r = api.login(self.condata)
        response_data = r.json()

        self.assertIsNotNone(len(response_data["access_token"]), "access_token is missing from response")
        self.assertGreater(len(response_data["access_token"]), 0, "access_token's length should be greater than 0")
        self.assertTrue(r.ok)

    # TestCase 5
    def test_send_message_non_existing_room(self):
        api.login(self.condata)
        r = api.send_message(self.condata, "!VurgtrNIhiKZAYJtjX:testing-techniques")
        response_data = r.json()
        self.assertEqual(response_data["error"], "Unknown room")
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertFalse(r.ok)

    # TestCase 6
    def test_create_room(self):
        api.login(self.condata)
        r = api.create_room(self.condata)
        response_data = r.json()
        self.assertIsNotNone(len(response_data["room_id"]), "room_id is missing from response")
        self.assertTrue(r.ok)

        state = api.get_state(self.condata)
        self.assertIsNotNone(state["rooms"]["join"][response_data["room_id"]])

    # TestCase 7
    def test_send_message(self):
        message = "hello this is a test message :D\n"

        api.login(self.condata)
        r = api.create_room(self.condata)
        room_id = r.json()["room_id"]

        r = api.send_message(self.condata, room_id, message)
        event_id = r.json()["event_id"]

        self.assertIsNotNone(
            len(event_id), "event_id is missing from response")
        self.assertTrue(r.ok)

        state = api.get_state(self.condata)
        message_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == event_id and event["content"]["body"] == message:
                message_found = True
                break
        self.assertTrue(message_found)    

    # TestCase 8
    def test_edit_message(self):
        new_message = "i have been \nedited \na \nlot"
        api.login(self.condata)
        r = api.create_room(self.condata)
        room_id = r.json()["room_id"]

        r = api.send_message(self.condata, room_id)
        event_id_send = r.json()["event_id"]

        r = api.edit_message(self.condata, room_id, event_id_send, new_message)
        event_id_edit = r.json()["event_id"]

        self.assertIsNotNone(
            len(r.json()["event_id"]), "event_id is missing from response")
        self.assertTrue(r.ok)

        state = api.get_state(self.condata)
        edit_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == event_id_edit and event["content"]["body"] == new_message:
                edit_found = True
                break
        self.assertTrue(edit_found)

    # TestCase 9
    def test_redact_message(self):
        api.login(self.condata)
        r = api.create_room(self.condata)
        room_id = r.json()["room_id"]

        r = api.send_message(self.condata, room_id)
        event_id_send = r.json()["event_id"]

        r = api.redact_message(self.condata, room_id, event_id_send)
        event_id_redact = r.json()["event_id"]

        self.assertIsNotNone(len(event_id_redact),
                             "event_id is missing from response")
        self.assertTrue(r.ok)

        state = api.get_state(self.condata)
        redact_found = False
        for event in state["rooms"]["join"][room_id]["timeline"]["events"]:
            if event["type"] == "m.room.redaction" and event["event_id"] == event_id_redact:
                redact_found = True
                break
        self.assertTrue(redact_found)

    # TestCase 10
    def test_forget_room(self):
        api.login(self.condata)
        r = api.create_room(self.condata)
        response_data = r.json()
        api.leave_room(self.condata, response_data["room_id"])
        r = api.forget_room(self.condata, response_data["room_id"])
        self.assertTrue(r.ok)

    # TestCase 11
    def test_leave_room(self):
        api.login(self.condata)
        r = api.create_room(self.condata)
        response_data = r.json()
        r = api.leave_room(self.condata, response_data["room_id"])
        self.assertTrue(r.ok)

        state = api.get_state(self.condata)
        self.assertRaises(
            KeyError, lambda: state["rooms"]["join"][response_data["room_id"]])

    # TestCase 12
    def test_edit_message_after_leaving_room(self):
        new_message = "i have been \nedited \na \nlot"
        api.login(self.condata)
        r = api.create_room(self.condata)
        room_id = r.json()["room_id"]

        r = api.send_message(self.condata, room_id)
        event_id_send = r.json()["event_id"]

        api.leave_room(self.condata, room_id)

        r = api.edit_message(self.condata, room_id, event_id_send, new_message)
        response_data = r.json()

        self.assertFalse(r.ok)
        self.assertEqual(response_data["errcode"], "M_FORBIDDEN")
        self.assertTrue(response_data["error"].__contains__("not in room " + room_id))

if __name__ == '__main__':
    unittest.main()
