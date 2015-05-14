from django.test import TestCase

from sbtv.settings import fixture_matches_url
from sbtv.football.util.decorators import pass_filtered_data_from_url


class DecoratorTest(TestCase):
    def setUp(self):
        @pass_filtered_data_from_url(fixture_matches_url)
        def decorated_fn(data):
            return data

        self.data = decorated_fn()

    def test_return_is_dict(self):
        self.assertIsInstance(
            self.data
            , list
        )
