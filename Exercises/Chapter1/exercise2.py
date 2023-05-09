#Construct a class hierarchy for different types of computers.

class Computer:
    def __init__(self, name, brand, model, year):
        self.name = name
        self.brand = brand
        self.model = model
        self.year = year

class Desktop(Computer):
    def __init__(self, name, brand, model, year, processor, ram, storage):
        super().__init__(name, brand, model, year)
        self.processor = processor
        self.ram = ram
        self.storage = storage

class Portable(Computer):
    def __init__(self, name, brand, model, year, processor, ram,storage, weight):
        super().__init__(name,brand,model,year)
        self.processor = processor
        self.ram = ram
        self.storage = storage 
        self.weight = weight

class Laptop(Portable):
    def __init__(self, name, brand, model, year, processor, ram,storage, weight, battery):
        super().__init__(name,brand,model,year,processor,ram,storage,weight)
        self.battery = battery

class Tablet(Portable):
    def __init__(self, name, brand, model, year, processor, ram,storage, weight, battery):
        super().__init__(name,brand,model,year,processor,ram,storage,weight)
        self.battery = battery

