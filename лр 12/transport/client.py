class Client:
    def __init__(self, name, cargo_weight, is_vip=False):
        if name:
            self.name = name
        else:
            raise ValueError("Имя должно быть указано!")
        try:
            cargo_weight = int(cargo_weight)
            self.cargo_weight = cargo_weight
        except ValueError:
            raise ValueError("Вес груза должен быть указан числом")
        if not (is_vip == True or is_vip == False):
            raise ValueError("Флаг VIP статуса указывается типом bool")
        self.is_vip = bool(is_vip)

    def __str__(self):
        return f"Client(Name: {self.name}, Cargo Weight: {self.cargo_weight}, VIP: {self.is_vip})"
