class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}')
my_car1 = Car('Ford', 'Mustang', 1964)
my_car2 = Car(brand='Tesla', model='s', year=2024)
my_car1.display_info()
my_car2.display_info()
