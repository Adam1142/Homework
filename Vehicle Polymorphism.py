class BMW:
    def fuel_type(self):
        print("BMW uses Petrol.")

    def max_speed(self):
        print("BMW's max speed is 300 km/h.")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Diesel.")

    def max_speed(self):
        print("Ferrari's max speed is 370 km/h.")

def car_details(car):
    car.fuel_type()
    car.max_speed()

bmw_car = BMW()
ferrari_car = Ferrari()

print("BMW Details:")
car_details(bmw_car)

print("Ferrari Details:")
car_details(ferrari_car)