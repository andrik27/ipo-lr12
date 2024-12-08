from .vehicle import Vehicle  # Импорт базового класса Vehicle

class Train(Vehicle):
    def __init__(self, capacity, number_of_cars, vehicle_id=None, current_load=0, clients_list=None):
        super().__init__(capacity, vehicle_id, current_load, clients_list)  # Вызов конструктора базового класса
        self.number_of_cars = number_of_cars

    def __str__(self):
        return f'Train ID: {self.vehicle_id}, Number of Cars: {self.number_of_cars}, Capacity: {self.capacity} tons, Current Load: {self.current_load} tons'
