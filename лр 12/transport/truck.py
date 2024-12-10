from .vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color, current_load=0):
        super().__init__(capacity, current_load)
        self.color = color

    def __str__(self):
        return f"Truck(ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load}, Color: {self.color})"
