# Return Data
from pipeline import transformer

def printReport(data: list):
    for item in data:
        print(f"OrderID: {item.orderID}"
              f"Product: {item.product}"
              f"Quantity: {item.quantity}"
              f"Price: ${item.unit_price}"
              f"Date Ordered: {item.date_of_order[0]} {item.date_of_order[1]}, {item.date_of_order[2]}")
        if item.isResolved:
            print("Order Status: Arrived")
        else:
            print("Order Status: Not Arrived")
        print(f"Total Cost: ${transformer.calculateTotalPrice(item)}\n")

def locationInfo(data):
    for item in data:
        print(f"Location: {item[1].storeID}"
              f"Address: {item[1].address}"
              f"Phone Number: {item[1].phoneNumber}")
        if item[2]:
            print("Location Orders;")
            printReport(item[2])
            print(f"Total Location Cost: ${transformer.calculateFullTotalPrice(item[2])}\n")