import unittest
import requests
from HttpTrigger import main
from unittest import mock

class TestFunction (unittest.TestCase):
   
    def test_url(self):
        r = requests.get('https://api.gios.gov.pl/pjp-api/rest/aqindex/getIndex/296').json()
        output_blob = mock.Mock()
        response = main(r, output_blob)
        assert response.status_code == 200
        assert '296' in response.get_body().decode() 
        output_blob.set.assert_called()

if __name__ == '__main__':
   unittest.main()
