from .vehicle import Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars, current_load=0):
        super().__init__(capacity, current_load)
        self.number_of_cars = number_of_cars

    def __str__(self):
        return f"Train(ID: {self.vehicle_id}, Capacity: {self.capacity}, Current Load: {self.current_load}, Number of Cars: {self.number_of_cars})"
