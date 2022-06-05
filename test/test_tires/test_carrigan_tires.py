import unittest

from tires.carrigan_tires import CarriganTires

#tire wear values are between 0 and 1 inclusive
class TestCarriganTires(unittest.TestCase):
    def test_needs_service(self):
        tire_wear = [0.1, 0.5, 0.9, 0.7]
        # (∃i,tire_wear[i] >= 0.9) 
        tires = CarriganTires(tire_wear)
        self.assertTrue(tires.needs_service())

    def test_does_not_need_service(self):
        tire_wear = [0.3, 0.8, 0.1, 0.1]
        # ¬(∃i,tire_wear[i] >= 0.9)
        tires = CarriganTires(tire_wear)
        self.assertFalse(tires.needs_service())