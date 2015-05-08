import json
import iso8601
import re

from datetime import datetime
from django.test import TestCase

from .views import *

class RequirementTest(TestCase):

    def setUp(self):
        self.response = self.client.get('/')
        try:
            self.dict_content = self.dict_content = json.loads(self.response.content.decode('utf-8'))
        except:
            self.dict_content = None

    def test_url_ok(self):
        self.assertEqual(
            self.response.status_code, 200
            , "The view have an error"
        )

    def test_type_is_json_dict(self):
        self.assertEqual(
            self.response['Content-Type']
            , 'application/json'
            , "The response don't have a JSON content type"
        )
        
        self.assertIsInstance(
            self.dict_content
            , dict
            , "The JSON response isn't a dict"
        )

    def test_dict_key_datetime(self):
        self.assertTrue(
            ('datetime' in self.dict_content)
            , "Datetime isn't present in the JSON response"
        )
        
        self.assertRegexpMatches(
            self.dict_content['datetime']
            , r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+'
            , "The datetime key doesn't have a ISO 8601 format"
        )

        self.assertIsInstance(
            iso8601.parse_date(self.dict_content['datetime'])
            , datetime
            , "The datetime key can't be parsed to datetime object"
        )

    def test_dict_key_completed_in(self):
        self.assertTrue(
            'completed_in' in self.dict_content
            , "Datetime isn't present in the JSON response"
        )

        self.assertRegexpMatches(
            self.dict_content['completed_in']
            , r'\d+\.\d{4} segundos'
            , "The completed_in key doesn't have the correct format"
        )

        exec_time = float(re.sub(r'[^\d\.]*', '', self.dict_content['completed_in']))

        if self.response['X-Cache'] == 'HIT':
            self.assertLess(
                    exec_time
                    , 2
                    , 'With cache the time of load must be under 2 seconds'
            )
        else:
            self.assertGreaterEqual(
                    exec_time
                    , 2
                    , 'Without cache the time of load must be under 2 seconds'
            )
        
