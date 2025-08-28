# Assignment: Classes, Inheritance & Polymorphism

# ---------------------------
# Activity 1: Design Your Own Class
# ---------------------------

class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, percent):
        self.battery += percent
        if self.battery > 100:
            self.battery = 100
        print(f"Battery charged to {self.battery}%")

    def info(self):
        print(f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery}%")


# Inherited Class with extra features
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 10:
            print(f"🎮 Playing {game} on {self.brand} {self.model} with {self.cooling_system} cooling system")
            self.battery -= 10
        else:
            print("Battery too low! Please charge your phone.")


# ---------------------------
# Activity 2: Polymorphism Challenge
# ---------------------------

class Vehicle:
    def move(self):
        pass  # Will be overridden by child classes

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water")


# ---------------------------
# Program Execution
# ---------------------------

if __name__ == "__main__":
    # Activity 1 Demo
    print("\n--- Smartphone Demo ---")
    phone1 = Smartphone("Samsung", "Galaxy S23", 128, 85)
    gaming_phone = GamingPhone("Asus", "ROG Phone 6", 256, 60, "Liquid Cooling")

    phone1.info()
    phone1.call("0712345678")
    phone1.charge(10)

    gaming_phone.info()
    gaming_phone.play_game("PUBG Mobile")

    # Activity 2 Demo
    print("\n--- Vehicle Polymorphism Demo ---")
    vehicles = [Car(), Plane(), Boat()]
    for v in vehicles:
        v.move()
