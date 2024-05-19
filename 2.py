class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def save_to_file(self, filename):
        try:
            with open(filename, 'a') as file:
                file.write(f"{self.name},{self.floors}\n")
            print(f"Building '{self.name}' saved to {filename}.")
        except Exception as e:
            print(f"An error occurred while saving the building: {e}")

    @staticmethod
    def load_from_file(filename):
        buildings = []
        try:
            with open(filename, 'r') as file:
                for line in file:
                    name, floors = line.strip().split(',')
                    buildings.append(Building(name, int(floors)))
            print(f"Buildings loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")
        except Exception as e:
            print(f"An error occurred while loading the buildings: {e}")
        return buildings
    

building1 = Building("Empire State Building", 102)
building2 = Building("Burj Khalifa", 163)
building3 = Building("Eiffel Tower", 3)

filename = "buildings.txt"


building1.save_to_file(filename)
building2.save_to_file(filename)
building3.save_to_file(filename)

 
loaded_buildings = Building.load_from_file(filename)

    
for bldg in loaded_buildings:
    print(f"Building Name: {bldg.name}, Floors: {bldg.floors}")
