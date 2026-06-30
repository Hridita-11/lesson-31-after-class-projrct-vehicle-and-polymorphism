class BMW:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "BMW max speed: 250 km/h"
class Ferrari:
    def fuel_type(self):
        return "Petrol"
    def max_speed(self):
        return "Ferrari max speed: 340 km/h"
for car in (BMW(), Ferrari()):
    print(car.__class__.__name__)
    print("Fuel:", car.fuel_type())
    print("Speed:", car.max_speed())
    print()
