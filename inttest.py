import requests
import unittest
import json
from flatten_json import flatten
from HttpTrigger import *
from datetime import datetime
import re


class int_test(unittest.TestCase):
    def test(self):
       r = requests.get('https://olga-int.azurewebsites.net/api/HttpTrigger')
       assert r.status_code is 200

    def test2(self):
        expected=(requests.get('https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/296')).json()
        flat=flatten(expected)
        data = json.dumps(flat)
        r = (requests.get('https://olga-int.azurewebsites.net/api/HttpTrigger')).json()
        r=json.dumps(r)
        self.assertEqual(data, r)

    def test3(self):
        expected=datetime.today().strftime('%Y-%m-%d')
        list=str(list_blobs())
        pattern="\d{4}-\d{2}-\d{2}"
        match=re.findall(pattern,list)
        self.assertIn(expected,match)

if __name__ == '__main__':
   unittest.main()
