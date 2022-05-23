from battery.battery import Battery
from add_Years import addYears

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date   

    def needs_service(self): 
        #battery_serviced_date is the date on which battery should be serviced by 
        battery_serviced_date = addYears(self.last_service_date, 2)
        if battery_serviced_date < self.current_date:
            return True
        else:
            return False

