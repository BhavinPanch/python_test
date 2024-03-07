class ShoppingCart:
    def __init__(self):
        self.prices = {"Apple": 0.60, "Orange": 0.25}
        self.items = []

    def scan(self, item):
        self.items.append(item)

    def calculate_total(self):
        apple_count = self.items.count('Apple')
        orange_count = self.items.count('Orange')

        # Buy one, get one free on apples
        apple_cost = (apple_count // 2 + apple_count % 2) * self.prices['Apple']

        # 3 for the price of 2 on oranges
        orange_cost = (orange_count // 3 * 2 + orange_count % 3) * self.prices['Orange']

        total_cost = apple_cost + orange_cost
        return round(total_cost, 2)
