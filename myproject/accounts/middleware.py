import time
from django.conf import settings

class DebugRequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            print(f"Request: {request.method}{request.path}")
            print(f"Headers: {request.headers}")
            print(f"Body: {request.body}")
            print(f"Cookies: {request.COOKIES}")
            print(f"Cookies: {request.POST}")

        response = self.get_response(request)

        if settings.DEBUG:
            print(f"Response: {request.method} {request.path} -> {response.status_code}")
        return response


class RequestTimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration = time.perf_counter() - start_time
        duration_ms = round(duration * 1000, 2)

        if settings.DEBUG:
            print(f"-> Method: {request.method}  -> Path: {request.path}")
            print(f"-> Status: {response.status_code}")
            print(f"-> Duration: {duration_ms} ms")

        return response
