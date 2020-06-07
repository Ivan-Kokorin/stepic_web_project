def application(environ, start_response):
    data = environ.get('QUERY_STRING')
    data_split = data.split("&")
    res = ""
    for i in data_split:
      res += i + "\n"
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter([bytes(res, "utf-8")])
