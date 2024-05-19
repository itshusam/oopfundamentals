#1
class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner


vehicle1 = Vehicle("hi321", "Car", "Alice")
vehicle2 = Vehicle("wow123", "Truck", "david")
print(f"Vehicle 1 (Registration: {vehicle1.registration_number}, Type: {vehicle1.type}) is owned by {vehicle1.owner}.")
print(f"Vehicle 2 (Registration: {vehicle2.registration_number}, Type: {vehicle2.type}) is owned by {vehicle2.owner}.")

vehicle1.update_owner("sammy")
print(f"Vehicle 1 (Registration: {vehicle1.registration_number}, Type: {vehicle1.type}) is owned by {vehicle1.owner}.")

#2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Total participants: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

event = Event("Python Workshop", "2024-06-01")

event.add_participant()
event.add_participant()

print(f"Current number of participants: {event.get_participant_count()}")
