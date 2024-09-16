import logging
import uuid

try:
    from asgiref.local import Local
except ImportError:
    from threading import local as Local    # noqa


local = Local()


class RequestIDFilter(logging.Filter):

    def filter(self, record):
        record.request_id = getattr(local, 'request_id', uuid.uuid4())
        return True
