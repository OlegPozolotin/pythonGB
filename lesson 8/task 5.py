
class Warehouse:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.inventory:
            if self.inventory[item] > quantity:
                self.inventory[item] -= quantity
            else:
                del self.inventory[item]

    def transfer_item(self, item, quantity, department):
        if item in self.inventory and self.inventory[item] >= quantity:
            self.inventory[item] -= quantity
            department.receive_item(item, quantity)
        else:
            print("Insufficient quantity of", item)

class OfficeEquipment:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Printer(OfficeEquipment):
    def __init__(self, brand, model, print_type):
        super().__init__(brand, model)
        self.print_type = print_type

class Scanner(OfficeEquipment):
    def __init__(self, brand, model, scan_resolution):
        super().__init__(brand, model)
        self.scan_resolution = scan_resolution

class Copier(OfficeEquipment):
    def __init__(self, brand, model, copy_speed):
        super().__init__(brand, model)
        self.copy_speed = copy_speed

class Department:
    def __init__(self, name):
        self.name = name
        self.equipment = {}

    def receive_item(self, item, quantity):
        if item in self.equipment:
            self.equipment[item] += quantity
        else:
            self.equipment[item] = quantity

# Пример использования классов
warehouse = Warehouse()
department = Department("IT Department")

printer = Printer("Epson", "L3150", "Inkjet")
scanner = Scanner("Canon", "CanoScan LiDE 400", "4800 dpi")
copier = Copier("Xerox", "WorkCentre 6515", "25 ppm")

warehouse.add_item(printer, 5)
warehouse.add_item(scanner, 3)
warehouse.add_item(copier, 2)

# Вывод списка оргтехники на складе
print("Warehouse inventory:")
for item, quantity in warehouse.inventory.items():
    print(type(item).__name__ + ": " + item.brand + " " + item.model + " - Quantity:", quantity)

# Передача оргтехники в отдел
warehouse.transfer_item(printer, 2, department)
warehouse.transfer_item(scanner, 1, department)

# Вывод списка оргтехники в отделе
print("\nDepartment inventory (" + department.name + "):")
for item, quantity in department.equipment.items():
    print(type(item).__name__ + ": " + item.brand + " " + item.model + " - Quantity:", quantity)
