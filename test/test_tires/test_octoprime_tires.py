import unittest

from tires.octoprime_tires import OctoprimeTires

class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.6, 0.9, 0.8, 0.9]
        #sum(tire_wear) >= 3.0 ==> True, then needs service
        tires = OctoprimeTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.3, 0.1, 0.1, 0.2]
        #sum(tire_wear) >= 3.0 ==> False, then does not need service
        tires = OctoprimeTires(tire_wear)
        self.assertFalse(tires.needs_service())