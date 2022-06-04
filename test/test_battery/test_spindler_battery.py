import unittest
import datetime

from battery.spindler_battery import SpindlerBattery

#Battery needs a service only if the battery_serviced_date < current_date
#battery_serviced_date = addYears(self.last_service_date, 2)
class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service(self):
        #last_service_date.replace(year=last_service_date.year + 2)  < current_date : True
        current_date = datetime.datetime(2022, 6, 4)
        last_service_date = datetime.datetime(2017, 5, 13)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_does_not_need_service(self):
        #last_service_date.replace(year=last_service_date.year + 2)  < current_date : False
        current_date = datetime.datetime(2022, 6, 4)
        last_service_date = datetime.datetime(2021 ,5, 13)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())