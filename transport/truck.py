from .vehicle import Vehicle  # Импорт класса Vehicle

class Truck(Vehicle):
    def __init__(self, capacity, color, vehicle_id=None, current_load=0, clients_list=None):
        super().__init__(capacity, vehicle_id, current_load, clients_list)  # Вызов конструктора базового класса
        self.color = color

    def __str__(self):
        return f'Truck ID: {self.vehicle_id}, Color: {self.color}, Capacity: {self.capacity} tons, Current Load: {self.current_load} tons'
