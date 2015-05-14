#!/usr/bin/python
# vim: set fileencoding=utf-8 :

import json
import re

from operator import itemgetter

from django.http import HttpResponse

from sbtv.football.util.decorators import pass_filtered_data_from_url
from sbtv.settings import fixture_matches_url


@pass_filtered_data_from_url(fixture_matches_url)
def matches(request, data):
    matches = []

    while len(data):
        match=data.pop()

        fmt_vs = "{} - {}"
        fechahora = match['fecha']+match['hora']

        matches.append({
            'partido': fmt_vs.format(
                match['local']['nombre']
                , match['visitante']['nombre']
            )
            , 'fecha': re.sub(
                r'^(\d{4})(\d{2})(\d{2})(\d{2}:\d{2}):00'
                , r'\4 \3-\2-\1'
                , fechahora
            )
            , 'fecha_int': int(re.sub(
                r'\D', r''
                , fechahora
            ))
            , 'resultado': fmt_vs.format(
                match['goleslocal']
                , match['golesvisitante']
            )
            , 'ganador': 'Empate' if match['goleslocal'] == match['golesvisitante']
                         else match['nomGan']
        })

    matches = sorted(matches, key=itemgetter('fecha_int'))

    for match in matches:
        match.pop('fecha_int', None)

    response = HttpResponse(
            json.dumps({
                "partidos": matches
            })
            , content_type="application/json"
    )

    return response
