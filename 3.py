class Bus:
    city_name = "Nashville"
    base_fare = 2.50

    def __init__(self, route_number, passenger_capacity):
     
        self.route_number = route_number
        self.passenger_capacity = passenger_capacity

    def display_info(self):
        print(f"City: {Bus.city_name}")
        print(f"Base Fare: ${Bus.base_fare}")
        print(f"Route Number: {self.route_number}")
        print(f"Passenger Capacity: {self.passenger_capacity}")


   
bus1 = Bus(101, 50)
bus2 = Bus(202, 75)


print("Bus 1 Information:")
bus1.display_info()
print()

  
print("Bus 2 Information:")
bus2.display_info()
print()

   
print(f"City Name (accessed through class): {Bus.city_name}")
print(f"Base Fare (accessed through class): ${Bus.base_fare}")
print()


print(f"City Name (accessed through bus1): {bus1.city_name}")
print(f"Base Fare (accessed through bus1): ${bus1.base_fare}")
print(f"City Name (accessed through bus2): {bus2.city_name}")
print(f"Base Fare (accessed through bus2): ${bus2.base_fare}")