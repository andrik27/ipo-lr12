from .client import Client
from .vehicle import Vehicle

class TransportCompany:
    def __init__(self, name):
        self.name = name
        self.vehicles = []
        self.clients = []

    def add_vehicle(self, vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("vehicle must be an instance of Vehicle")
        self.vehicles.append(vehicle)

    def list_vehicles(self):
        return self.vehicles

    def add_client(self, client):
        if not isinstance(client, Client):
            raise TypeError("client must be an instance of Client")
        self.clients.append(client)

    def list_clients(self):
        return self.clients

    def optimize_cargo_distribution(self):
        priority = []
        not_priority = []
        success = []
        for self_client in self.clients:
            if self_client.is_vip:
                priority.append(self_client)
        for self_client in self.clients:
            if self_client not in priority:
                not_priority.append(self_client)
        for self_client in priority:
            for vehicle in self.vehicles:
                free_space = vehicle.capacity - vehicle.current_load
                weight = self_client.cargo_weight
                if free_space >= weight:
                    vehicle.current_load += weight
                    vehicle.clients_list.append(self_client)
                    success.append(self_client)
                    break
        for self_client in not_priority:
            for vehicle in self.vehicles:
                free_space = vehicle.capacity - vehicle.current_load
                weight = self_client.cargo_weight
                if free_space >= weight:
                    vehicle.current_load += weight
                    vehicle.clients_list.append(self_client)
                    success.append(self_client)
                    break
        print("Груз успешно оптимизирован и распределен для следующих клиентов компании:", end=" ")
        for client in success:
            print(f"{client.name}", end=" ")
        print()
