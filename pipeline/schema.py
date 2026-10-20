# Define Classes Here

class Order:
    def __init__(self, order_ID, product, unit_price, quantity,
                 provider, date_of_order=("October", 15, 2020), is_resolved=False):
        self.orderID = order_ID
        self.product = product
        self.unit_price = unit_price
        self.quantity = quantity
        self.provider = provider
        self.date_of_order = date_of_order
        self.resolved = is_resolved

    def isResolved(self):
        return self.resolved

    def resolve(self):
        self.resolved = True

    def unresolve(self):
        self.resolved = False

class Store:
    def __init__(self, store_ID, address, phone_number):
        self.storeID = store_ID
        self.address = address
        self.phoneNumber = phone_number