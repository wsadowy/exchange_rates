from scrapy.http import Response, Request


def fake_response(file_path):
    url = ''
    request = Request(url=url)
    with open(file_path, 'r') as f:
        response = Response(url=url,
                            request=request,
                            body=f.read())
        response.encoding = 'utf-8'
    return response
