class Warehouse:
    def __init__(self):
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)


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


# Пример использования классов
warehouse = Warehouse()

printer = Printer("Epson", "L3150", "Inkjet")
scanner = Scanner("Canon", "CanoScan LiDE 400", "4800 dpi")
copier = Copier("Xerox", "WorkCentre 6515", "25 ppm")

warehouse.add_item(printer)
warehouse.add_item(scanner)
warehouse.add_item(copier)

# Вывод списка оргтехники на складе
for item in warehouse.inventory:
    print(type(item).__name__ + ": " + item.brand + " " + item.model)

