import urllib.parse
import urllib.request
import urllib.error
import json
import zlib

from pygg.exception import PyGGError, APIError

api_key = ""
print_calls = False


def get(request, params={}, include_base=True):
    """Makes a rate-limited HTTP request to the Riot API and returns the result
    request         str               the request string
    params          dict<str, any>    the parameters to send with the request (default {})
    return          dict              the JSON response from the Champion.gg API as a dict
    """
    if not api_key:
        raise PyGGError("API Key must be set before the API can be queried.")

    # Encode params
    params["api_key"] = api_key
    encoded_params = urllib.parse.urlencode(params)

    # Build and execute request
    if include_base:
        url = "http://api.champion.gg/{request}?{params}".format(request=request, params=encoded_params)
    else:
        url = "{request}?{params}".format(request=request, params=encoded_params)

    try:
        content = execute_request(url)
        return json.loads(content)
    except urllib.error.HTTPError as error:
        raise APIError("Server returned error {code} on call: {url}".format(code=error.code, url=url), error.code)


def execute_request(url, method="GET", payload=""):
    """Executes an HTTP request and returns the result in a string
    url        str    the full URL to send a request to
    method     str    the HTTP method to use
    payload    str    the json payload to send if appropriate for HTTP method
    return     str    the content returned by the server
    """
    if print_calls:
        print(url)

    response = None
    try:
        if payload:
            payload = payload.encode("UTF-8")
            request = urllib.request.Request(url, method=method, payload=payload)
        else:
            request = urllib.request.Request(url, method=method)
        request.add_header("Accept-Encoding", "gzip")
        request.add_header("User-Agent", "Mozilla/5.0")
        response = urllib.request.urlopen(request)
        content = response.read()
        content = zlib.decompress(content, zlib.MAX_WBITS | 16).decode(encoding="UTF-8")
        return content
    finally:
        if response:
            response.close()
