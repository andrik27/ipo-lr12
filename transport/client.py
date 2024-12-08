class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        self.name = name  # Имя клиента
        self.cargo_weight = cargo_weight  # Вес груза клиента
        self.is_vip = is_vip  # Флаг VIP-статуса клиента

    def __str__(self):
        return f'Client {self.name} (VIP: {self.is_vip}) with cargo weight {self.cargo_weight} tons'
