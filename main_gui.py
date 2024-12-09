import tkinter as tk
from tkinter import messagebox, simpledialog
from transport.transport_company import TransportCompany
from transport.truck import Truck
from transport.train import Train
from transport.client import Client

class TransportApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Транспортная Компания")
        
        # Создание меню
        self.create_menu()

        # Панель управления
        self.create_controls()

        # Таблицы данных
        self.create_tables()

        # Инициализация объекта транспортной компании
        self.transport_company = TransportCompany("Global Transport")

        # Загрузка данных из файла и отображение в интерфейсе
        self.load_and_display_data()

        # Статусная строка
        self.status_bar = tk.Label(root, text="Готово", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # Меню "Файл"
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

    def create_controls(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        self.add_client_button = tk.Button(frame, text="Добавить клиента", command=self.add_client)
        self.add_client_button.pack(side=tk.LEFT, padx=5)

        self.add_vehicle_button = tk.Button(frame, text="Добавить транспорт", command=self.add_vehicle)
        self.add_vehicle_button.pack(side=tk.LEFT, padx=5)

        self.remove_client_button = tk.Button(frame, text="Удалить клиента", command=self.remove_client)
        self.remove_client_button.pack(side=tk.LEFT, padx=5)

        self.remove_vehicle_button = tk.Button(frame, text="Удалить транспорт", command=self.remove_vehicle)
        self.remove_vehicle_button.pack(side=tk.LEFT, padx=5)

        self.optimize_button = tk.Button(frame, text="Распределить грузы", command=self.optimize_cargo)
        self.optimize_button.pack(side=tk.LEFT, padx=5)

    def create_tables(self):
        self.clients_listbox = tk.Listbox(self.root, height=10, width=50)
        self.clients_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.vehicles_listbox = tk.Listbox(self.root, height=10, width=50)
        self.vehicles_listbox.pack(side=tk.RIGHT, padx=10, pady=10)

    def load_and_display_data(self):
        for client in self.transport_company.list_clients():
            self.clients_listbox.insert(tk.END, f"{client}")
        
        for vehicle in self.transport_company.list_vehicles():
            self.vehicles_listbox.insert(tk.END, f"{vehicle}")

    def add_client(self):
        # Открытие окна для добавления клиента
        self.status_bar.config(text="Добавление клиента")
        client_window = tk.Toplevel(self.root)
        client_window.title("Добавить клиента")
        
        tk.Label(client_window, text="Имя клиента").pack(pady=5)
        client_name_entry = tk.Entry(client_window)
        client_name_entry.pack(pady=5)

        tk.Label(client_window, text="Вес груза (в т)").pack(pady=5)
        cargo_weight_entry = tk.Entry(client_window)
        cargo_weight_entry.pack(pady=5)

        vip_status = tk.BooleanVar()
        tk.Checkbutton(client_window, text="VIP клиент", variable=vip_status).pack(pady=5)

        def save_client():
            name = client_name_entry.get()
            try:
                cargo_weight = float(cargo_weight_entry.get())
                if not name.isalpha() or len(name) < 2:
                    raise ValueError("Имя должно содержать только буквы и быть не менее 2 символов.")
                if cargo_weight <= 0 or cargo_weight > 1000:
                    raise ValueError("Вес груза должен быть положительным числом не более 1000 т.")
                
                client = Client(name, cargo_weight, vip_status.get())
                self.transport_company.add_client(client)
                self.clients_listbox.insert(tk.END, f"{client}")
                self.status_bar.config(text="Клиент добавлен")
                client_window.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка ввода", str(e))

        tk.Button(client_window, text="Сохранить", command=save_client).pack(pady=5)
        tk.Button(client_window, text="Отмена", command=client_window.destroy).pack(pady=5)

    def add_vehicle(self):
        # Открытие окна для добавления транспортного средства
        self.status_bar.config(text="Добавление транспортного средства")
        vehicle_window = tk.Toplevel(self.root)
        vehicle_window.title("Добавить транспортное средство")
        
        tk.Label(vehicle_window, text="Тип транспорта").pack(pady=5)
        vehicle_type_var = tk.StringVar()
        vehicle_type_var.set("Грузовик")
        tk.OptionMenu(vehicle_window, vehicle_type_var, "Грузовик", "Поезд").pack(pady=5)

        tk.Label(vehicle_window, text="Грузоподъемность (в т)").pack(pady=5)
        capacity_entry = tk.Entry(vehicle_window)
        capacity_entry.pack(pady=5)

        def save_vehicle():
            vehicle_type = vehicle_type_var.get()
            try:
                capacity = float(capacity_entry.get())
                if capacity <= 0:
                    raise ValueError("Грузоподъемность должна быть положительным числом")

                if vehicle_type == "Грузовик":
                    color = simpledialog.askstring("Цвет грузовика", "Введите цвет грузовика")
                    if not color:
                        raise ValueError("Цвет грузовика не может быть пустым")
                    vehicle = Truck(capacity, color)
                elif vehicle_type == "Поезд":
                    number_of_cars = simpledialog.askinteger("Количество вагонов", "Введите количество вагонов")
                    if number_of_cars <= 0:
                        raise ValueError("Количество вагонов должно быть положительным целым числом")
                    vehicle = Train(capacity, number_of_cars)

                self.transport_company.add_vehicle(vehicle)
                self.vehicles_listbox.insert(tk.END, f"{vehicle}")
                self.status_bar.config(text="Транспортное средство добавлено")
                vehicle_window.destroy()
            except ValueError as e:
                messagebox.showerror("Ошибка ввода", str(e))

        tk.Button(vehicle_window, text="Сохранить", command=save_vehicle).pack(pady=5)
        tk.Button(vehicle_window, text="Отмена", command=vehicle_window.destroy).pack(pady=5)

    def remove_client(self):
        selected_client_index = self.clients_listbox.curselection()
        if selected_client_index:
            client_name = self.clients_listbox.get(selected_client_index)
            self.transport_company.remove_client(client_name.split()[1])  # Извлекаем имя клиента из строки
            self.clients_listbox.delete(selected_client_index)
            self.status_bar.config(text="Клиент удален")
        else:
            messagebox.showwarning("Удаление клиента", "Пожалуйста, выберите клиента для удаления")

    def remove_vehicle(self):
        selected_vehicle_index = self.vehicles_listbox.curselection()
        if selected_vehicle_index:
            vehicle_id = self.vehicles_listbox.get(selected_vehicle_index).split()[2].replace(',', '')  # Удаление запятых
            self.transport_company.remove_vehicle(int(vehicle_id))
            self.vehicles_listbox.delete(selected_vehicle_index)
            self.status_bar.config(text="Транспортное средство удалено")
        else:
            messagebox.showwarning("Удаление транспортного средства", "Пожалуйста, выберите транспортное средство для удаления")

    def optimize_cargo(self):
        self.transport_company.optimize_cargo_distribution()
        self.status_bar.config(text="Грузы оптимизированы")
        messagebox.showinfo("Распределение грузов", "Грузы оптимизированы")

if __name__ == "__main__":
    root = tk.Tk()
    app = TransportApp(root)
    root.mainloop()
