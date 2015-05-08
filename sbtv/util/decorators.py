import json
from time import time
from datetime import datetime


def timestamp_and_exec_time_if_json_dict(fn):
    def dec_fn(*args, **kwargs):
        exec_time = time()
        response = fn(*args, **kwargs)
        exec_time = time() - exec_time

        try:
            resp_json_dict = json.loads(response.content.decode('utf-8'))

            if isinstance(resp_json_dict, dict):
                resp_json_dict['completed_in'] = '{:.4f} segundos'.format(exec_time)
                resp_json_dict['datetime'] = datetime.now().isoformat()

                response.content = json.dumps(resp_json_dict)
        except:
            pass

        return response

    return dec_fn
