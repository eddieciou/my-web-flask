import logging
from commons.Response import response


class Schedules:
    def __init__(self):
        pass
        self.logging = logging.getLogger(__name__)

    def get_schedules(self):
        self.logging.info("get_schedules")

        return response(0, "", {"result": "schedules"})
