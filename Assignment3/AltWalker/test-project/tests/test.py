import sys
# Modify the path there to point to the right directory
sys.path.append("C:/Users/svenv/OneDrive/Documenten/Uni/22-23/Testing Techniques/Assignment3/AltWalker/test-project/modules")

import apirequest as api
import constants

class Matrix:

    class ConnectionData:
        server_ip = constants.server_ip
        server_address = constants.server_ip
        access_token = ""
        room_id = ""
        send_event_id = ""
        edit_event_id = ""
        redact_event_id = ""
        message = "hello this is a test message :D"
        edit_message = "i have been \nedited \na \nlot"

    condata = ConnectionData

    # Gets executed before every model run; initiates the server address
    def setUpModel(self):
        self.condata.server_address = 'https://' + self.condata.server_ip + ':443/_matrix/client/v3'

    # Gets execuded after every model run; resets the test space
    def tearDownModel(self):
        r = api.get_state(self.condata)
        if "rooms" in r.json():
            for room_id in r.json()["rooms"]["join"]:

                try:
                    api.leave_room(self.condata, room_id)
                except:
                    print("leave failed for " + room_id)
                try:
                    api.forget_room(self.condata, room_id)
                except:
                    print("forget failed for " + room_id)
        api.logout(self.condata)


    # Nodes; test space is checked for correctness at every node
    def Logged_Out(self):
        r = api.get_state(self.condata)
        response_data = r.json()

        assert response_data["errcode"] == "M_UNKNOWN_TOKEN" or response_data["errcode"] == "M_MISSING_TOKEN"
        assert response_data["error"] == "Invalid access token passed." or response_data["error"] == 'Invalid Authorization header.'
    
    def Logged_In(self):
        r = api.get_state(self.condata)

        assert r.ok == True

    def Made_Room(self):
        # reset access token to get updated state
        r = api.login(self.condata)
        self.condata.access_token = r.json()["access_token"]

        r = api.get_state(self.condata)

        assert self.condata.room_id in r.json()["rooms"]["join"]

    def Room_Left(self):
        # reset access token to get updated state
        r = api.login(self.condata)
        self.condata.access_token = r.json()["access_token"]

        r = api.get_state(self.condata)
        try:
            r.json()["rooms"]["join"][self.condata.room_id]
            assert False, "room id found in the state even though it should be left"
        except:
            assert True

    def Message_Edited(self):
        # reset access token to get updated state
        r = api.login(self.condata)
        self.condata.access_token = r.json()["access_token"]

        r = api.get_state(self.condata)
        edit_found = False
        for event in r.json()["rooms"]["join"][self.condata.room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == self.condata.edit_event_id and event["content"]["body"] == self.condata.edit_message:
                edit_found = True
                break
        assert edit_found

    def Message_Sent(self):
        # reset access token to get updated state
        r = api.login(self.condata)
        self.condata.access_token = r.json()["access_token"]

        r = api.get_state(self.condata)
        message_found = False
        for event in r.json()["rooms"]["join"][self.condata.room_id]["timeline"]["events"]:
            if event["type"] == "m.room.message" and event["event_id"] == self.condata.send_event_id and event["content"]["body"] == self.condata.message:
                message_found = True
                break
        assert message_found

    def Message_Redacted(self):
        # reset access token to get updated state
        r = api.login(self.condata)
        self.condata.access_token = r.json()["access_token"]

        r = api.get_state(self.condata)
        redact_found = False
        for event in r.json()["rooms"]["join"][self.condata.room_id]["timeline"]["events"]:
            if event["type"] == "m.room.redaction" and event["event_id"] == self.condata.redact_event_id:
                redact_found = True
                break
        assert redact_found



    # Edges; at every edge an api call is made, the response is checked and the connection data is updated
    def log_in(self):
        r = api.login(self.condata)

        assert r.ok
        assert "access_token" in r.json()

        self.condata.access_token = r.json()["access_token"]


    def log_out(self):
        r = api.logout(self.condata)

        assert r.ok

        self.condata.access_token = ""

    def create_room(self):
        r = api.create_room(self.condata)

        assert r.ok
        assert "room_id" in r.json()

        self.condata.room_id = r.json()["room_id"]


    def leave_room(self):
        r = api.leave_room(self.condata, self.condata.room_id)

        assert r.ok

    def forget_room(self):        
        r = api.forget_room(self.condata, self.condata.room_id)

        assert r.ok

        self.condata.room_id = ""

    def send_message(self):
        r = api.send_message(self.condata, self.condata.room_id, self.condata.message)

        assert r.ok
        assert "event_id" in r.json()

        self.condata.send_event_id = r.json()["event_id"]


    def edit_message(self):
        r = api.edit_message(self.condata, self.condata.room_id, self.condata.send_event_id, self.condata.edit_message)

        assert r.ok

        self.condata.edit_event_id = r.json()["event_id"]

    def redact_message(self):
        r = api.redact_message(self.condata, self.condata.room_id, self.condata.send_event_id)

        assert r.ok

        self.condata.redact_event_id = r.json()["event_id"]

    def tau(self):
        pass
