from datetime import datetime
from collections import deque

class Product:
    def __init__(self, name, category, size, price, batch_number, expiry_date):
        self.name = name
        self.category = category
        self.size = size
        self.price = price
        self.batch_number = batch_number
        self.expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d")  # Expiry date format: YYYY-MM-DD
        self.stock_level = 0
        self.sales = 0
        self.batch_data = deque()  # FIFO structure to manage stock batches

    def update_stock(self, quantity, batch_number, expiry_date):
        # Add new stock with batch info to FIFO queue
        self.batch_data.append({'quantity': quantity, 'batch_number': batch_number, 'expiry_date': expiry_date})
        self.stock_level += quantity

    def sell(self, quantity):
        if quantity <= self.stock_level:
            # Ensure FIFO (First In, First Out) by selling from the earliest batch
            sold_quantity = 0
            while quantity > 0 and self.batch_data:
                batch = self.batch_data[0]
                if batch['quantity'] >= quantity:
                    batch['quantity'] -= quantity
                    sold_quantity += quantity
                    quantity = 0
                else:
                    quantity -= batch['quantity']
                    sold_quantity += batch['quantity']
                    self.batch_data.popleft()  # Remove exhausted batch
            self.stock_level -= sold_quantity
            self.sales += sold_quantity
            return True
        else:
            return False  # Not enough stock to sell

    def check_expiry(self):
        # Check if any batch is expired (before the current date)
        expired_batches = []
        current_date = datetime.now()
        for batch in self.batch_data:
            if batch['expiry_date'] < current_date:
                expired_batches.append(batch)
        return expired_batches

