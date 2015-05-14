import urllib.request
import xml.sax

from sbtv.util.decorators import timestamp_and_exec_time_if_json_dict
from sbtv.football.util.saxparsers import MatchesHandler

def pass_filtered_data_from_url(fixture_xml_url, parser=None):
    def superwrap(fn):
        @timestamp_and_exec_time_if_json_dict
        def dec_fn(*args, **kwargs):
            http_xml_handle = urllib.request.urlopen(fixture_xml_url)

            items = list()

            xml.sax.parse(
                http_xml_handle
                , MatchesHandler(items)
            )

            kwargs['data'] = items

            r=fn(*args, **kwargs)
            return r

        return dec_fn
    return superwrap
