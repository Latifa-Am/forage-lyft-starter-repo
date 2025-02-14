from serviceable import Serviceable

#Since there is a composition relashionship between Car and Battery/Engine, so 
# we'll be creating instances (engine/battery) for the component class (Car) 
class Car(Serviceable):
    def __init__(self, engine, battery, tires):
        self.engine = engine
        self.battery=battery
        self.tires = tires

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()
