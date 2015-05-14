import xml.etree.ElementTree as XMLElementTree

from django.test import TestCase

from sbtv.settings import fixture_matches_url
from sbtv.football.util.funcs import HttpRemoteResponse


class FixtureXMLTest(TestCase):

    def setUp(self):
        self.fixture_xml_response = HttpRemoteResponse(fixture_matches_url)
        self.fixture_xml_etree = None

    def test_url_xml(self):
        self \
            .chain_test_url_xml_parse() \
            .chain_test_url_xml_is_fixture() \


    def chain_test_url_xml_parse(self):
        self.fixture_xml_etree = XMLElementTree.fromstring(
            self.fixture_xml_response.content
        )

        return self

    def chain_test_url_xml_is_fixture(self):
        xml_root_element = self.fixture_xml_etree

        self.assertEqual(
            xml_root_element.tag
            , 'fixture'
            , 'The XML data from the url {0} isn\'t a fixture'.format(fixture_matches_url)
        )