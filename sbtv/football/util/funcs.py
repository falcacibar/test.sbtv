from django.http import HttpResponse
import urllib


def HttpRemoteResponse(url):
    response = urllib.request.urlopen(url)

    # set the body
    r = HttpResponse(response.read())

    # set the headers
    for header in response.info().keys():
        r[header] = response.info()[header]

    return r
