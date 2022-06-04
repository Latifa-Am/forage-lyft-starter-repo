import unittest

from engine.capulet_engine import CapuletEngine

#Engine needs a service only if the current mileage - last service mileage > 30000
class TestCapuletEngine(unittest.TestCase):
    def test_needs_service(self):
        #30001 - 0 > 30000 : True
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_does_not_need_service(self):
        #30000 - 0 > 30000 : False
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())