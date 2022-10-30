from distutils.cmd import Command
import json
import unittest
import requests

class MatrixTestingClass(unittest.TestCase):

    server_ip = '192.168.0.170'
    server_address = ''

    def setUp(self):
        self.server_address = 'https://' + self.server_ip + ':443/_matrix/client/v3'

    def test_valid_login(self):
        command = "/login"
        request_url = self.server_address + command
        request_parameters = {
            "identifier": {
                "type": "m.id.user", 
                "user": "matrixadmin"
                }, 
            "initial_device_display_name": "Jungle Phone", 
            "password": "admin", "type": "m.login.password"
        }
        r = requests.post(url = request_url, data = json.dumps(request_parameters), verify=False)
        response_data = r.json()
        self.assertIsNotNone(len(response_data["access_token"]), "access_token is missing from response")
        self.assertGreater(len(response_data["access_token"]), 0, "access_token's length should be greater than 0")

if __name__ == '__main__':
    unittest.main()