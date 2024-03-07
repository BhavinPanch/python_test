class ShoppingCart:
    def __init__(self):
        self.prices = {"Apple": 0.60, "Orange": 0.25}
        self.items = []

    def scan(self, item):
        self.items.append(item)

    def calculate_total(self):
        total_cost = 0
        for item in self.items:
            total_cost += self.prices.get(item, 0)
        return round(total_cost, 2)
