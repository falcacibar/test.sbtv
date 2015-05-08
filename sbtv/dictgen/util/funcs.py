import itertools
import random


def randomdict(str_dict, dict_len, key_len=1, value_len=1):
    return dict(
        (randomstr(str_dict, key_len), randomstr(str_dict, value_len))
        for _ in itertools.repeat(None, dict_len)
    )


def randomstr(str_dict, str_len):
    str = ''

    for _ in itertools.repeat(None, str_len):
        str += random.choice(str_dict)

    return str
