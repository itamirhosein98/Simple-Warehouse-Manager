class phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def power_button(self):
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        print(f"{self.brand} {self.model} is now OFF.")
my_phone = phone('Apple', 'iPhone 13', 999)
my_phone.power_button()
my_phone.power_off()
