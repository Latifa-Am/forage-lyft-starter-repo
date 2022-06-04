import unittest

from engine.willoughby_engine import WilloughbyEngine

#Engine needs a service only if the current mileage - last service mileage > 60000
class TestWilloughbyEngine(unittest.TestCase):
    def test_needs_service(self):
        #60001 - 0 > 60001 : True
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        #60000 - 0 > 60000 : False
        current_mileage = 60000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())