from django.test import TestCase

from sbtv.util.test import CommonViewTest
from sbtv.util.test import CommonJSONViewTest

from ..views import *


class MatchesViewTest(TestCase, CommonJSONViewTest, CommonViewTest):

    JSONMustBe = dict

    def setUp(self):
        self.response = self.client.get('/futbol/')
        try:
            self.dict_content = json.loads(self.response.content.decode('utf-8'))
        except:
            self.dict_content = None
