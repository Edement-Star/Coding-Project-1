# Return Data
from pipeline import transformer

def printReport(data: list):
    if isinstance(data, list):
        for item in data:
            print(f"OrderID: {item.orderID}\n"
                  f"Product: {item.product}\n"
                  f"Quantity: {item.quantity}\n"
                  f"Price: ${item.unit_price}\n"
                  f"Date Ordered: {item.date_of_order[0]} {item.date_of_order[1]}, {item.date_of_order[2]}")
            if item.isResolved():
                print("Order Status: Arrived")
            else:
                print("Order Status: Not Arrived")
            print(f"Total Cost: ${round(transformer.calculateTotalPrice(item),2)}\n")
    else:
        print(f"OrderID: {data.orderID}\n"
              f"Product: {data.product}\n"
              f"Quantity: {data.quantity}\n"
              f"Price: ${data.unit_price}\n"
              f"Date Ordered: {data.date_of_order[0]} {data.date_of_order[1]}, {data.date_of_order[2]}")
        if data.isResolved():
            print("Order Status: Arrived")
        else:
            print("Order Status: Not Arrived")
        print(f"Total Cost: ${round(transformer.calculateTotalPrice(data),2)}\n")

def storeInfo(data: list):
    print(f"Location: {data[0].storeID}\n"
          f"Address: {data[0].address}\n"
          f"Phone Number: {data[0].phoneNumber}\n")

    print("Location Orders;")
    printReport(data[1])

def locationInfo(data):
    for item in data:
        storeInfo(item)
