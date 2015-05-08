import json

from time import sleep

from django.http import HttpResponse
from django.core.cache import caches

from sbtv.util.decorators import timestamp_and_exec_time_if_json_dict
from sbtv.dictgen.util.funcs import randomdict


@timestamp_and_exec_time_if_json_dict
def dictgen(request):
    cache = caches['default']
    x_cache = 'MISS'

    if 'dictgen_dict' in cache:
        dict = cache.get('dictgen_dict')
        x_cache = 'HIT'
    else:
        dict = randomdict(
                    str_dict='abcdefghijklmnopqrstuvwxyz1234567890'
                    , dict_len=50
                    , key_len=4
                    , value_len=15
        )

        # Si el retraso lo pongo despues, ya me consumo 2 segundos de caché
        # lo cual no es lo que se espera.
        sleep(2)

        cache.set('dictgen_dict', dict, 5)

    response = HttpResponse(
            json.dumps(dict)
            , content_type="application/json"
    )

    response['X-Cache'] = x_cache

    return response
