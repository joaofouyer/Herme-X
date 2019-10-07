import json
import requests
from requests.utils import get_unicode_from_response
from django.conf import settings


def sync(mode, data):
    try:
        if len(data) > 1000:
            remaining = len(data)
            start, end = 0, 1000
            remaining = remaining - end
            chunk = data[start:end]
            while remaining:
                response = requests.post("{url}/sync/{mode}".format(url=settings.LOCATION_URL, mode=mode), json=chunk)
                if response.status_code == 200:
                    start = end
                    if remaining > 1000:
                        end = end + 1000
                        remaining = remaining - 1000
                    else:
                        end + remaining
                        remaining = 0
                    chunk = data[start:end]
                else:
                    return True

        else:
            response = requests.post("{url}/sync/{mode}".format(url=settings.LOCATION_URL, mode=mode), json=data)
            if response.status_code == 200:
                response = json.loads(get_unicode_from_response(response))
                print(response)
                return None

    except Exception as e:
        print("Exception on location webservice sync: {} {}".format(type(e), e))
        raise e
