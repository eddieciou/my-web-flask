import logging
from commons.Response import response


class MobileRequest:
    def __init__(self):
        self.logging = logging.getLogger(__name__)

    def mobile_request(self):
        self.logging.info('mobile_request')

        return response(0, "", {"result": "mobile request"})
