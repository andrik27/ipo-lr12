from .client import Client  # Импорт класса Client

class Vehicle:
    next_id = 1  # Статическая переменная для генерации ID

    def __init__(self, capacity, vehicle_id=None, current_load=0, clients_list=None):
        if vehicle_id is None:
            self.vehicle_id = f"{Vehicle.next_id}"  # Генерация нового ID
            Vehicle.next_id += 1
        else:
            self.vehicle_id = vehicle_id  # Использование существующего ID

        self.capacity = capacity  # Грузоподъемность транспортного средства
        self.current_load = current_load  # Текущая загрузка
        self.clients_list = clients_list if clients_list is not None else []  # Список клиентов

    def load_cargo(self, client):
        if not isinstance(client, Client):
            raise ValueError("Invalid client")  # Проверка типа клиента
        if self.current_load + client.cargo_weight > self.capacity:
            raise ValueError("Capacity exceeded")  # Проверка грузоподъемности
        self.current_load += client.cargo_weight  # Увеличение текущей загрузки
        self.clients_list.append(client)  # Добавление клиента в список

    def __str__(self):
        return f'Vehicle ID: {self.vehicle_id}, Capacity: {self.capacity} tons, Current Load: {self.current_load} tons'
