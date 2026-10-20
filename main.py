import random
from pipeline import *
from pipeline import schema
from pipeline import validator
from pipeline import transformer
from pipeline import reporter
from pipeline.schema import Order

order_data = validator.correctData(ORDERS)
order_list = []
store_list = []
location_data = [[[]],[[]],[[]]]

#Construct Orders
for i in range(len(order_data)):
    if "Date Ordered" not in order_data[i] and "Resolved" not in order_data[i]:
        new_order = schema.Order(i + 1, order_data[i]["Product"], order_data[i]["Unit Price"],order_data[i]["Quantity"],
                                 order_data[i]["Provider"])
    elif "Date Ordered" not in order_data[i]:
        new_order = schema.Order(i + 1, order_data[i]["Product"], order_data[i]["Unit Price"],
                                 order_data[i]["Quantity"], order_data[i]["Provider"], ("October", 15, 2020), order_data[i]["Resolved"])
    elif "Resolved" not in order_data[i]:
        new_order = schema.Order(i + 1, order_data[i]["Product"], order_data[i]["Unit Price"],
                                 order_data[i]["Quantity"], order_data[i]["Provider"], order_data[i]["Date Ordered"])
    else:
        new_order = schema.Order(i+1, order_data[i]["Product"], order_data[i]["Unit Price"], order_data[i]["Quantity"],
                                 order_data[i]["Provider"], order_data[i]["Date Ordered"], order_data[i]["Resolved"])
    order_list.append(new_order)

x=0
#Construct Stores
for store in STORES:
    x += 1
    new_store = schema.Store(x, store['Address'], store['Phone'])
    store_list.append(new_store)

#Randomize Location Data
for i in range(len(store_list)):
    location_data[i].insert(0, store_list[i])
for order in order_list:
    random_store = random.randint(0, len(store_list)-1)
    location_data[random_store][1].append(order)

loop = True
while loop:
    print("1. Check Individual Order")
    print("2. Check All Orders")
    print("3. Check Unresolved Orders")
    print("4. Check Resolved Orders")
    print("5. Check Store Data")
    print("6. Check All Locations")
    print("7. Resolve Order")
    print("8. Unresolve Order")
    print("9. Exit\n")
    choice = input("Enter your choice: ")
    print("\n")

    if choice == "1":
        choice1 = True
        while choice1:
            try:
                order_number = int(input('Choose a number (1-10): '))
                print('')
            except ValueError:
                print("Please enter a valid number.")
            else:
                if order_number >= 1 and order_number <= 10:
                    reporter.printReport(order_list[order_number-1])
                    choice1 = False
                else:
                    print("Please enter a valid number.")
            finally:
                input("Press Enter to continue...\n")
    elif choice == "2":
        reporter.printReport(order_list)
        input("Press Enter to continue...\n")
    elif choice == "3":
        for order in order_list:
            if not order.isResolved():
                reporter.printReport(order)
        input("Press Enter to continue...\n")
    elif choice == "4":
        for order in order_list:
            if order.isResolved():
                reporter.printReport(order)
        input("Press Enter to continue...\n")
    elif choice == "5":
        choice5 = True
        while choice5:
            try:
                store_number = int(input('Choose a number (1-3): '))
                print('')
            except ValueError:
                print("Please enter a valid number.")
            else:
                if store_number >= 1 and store_number <= 3:
                    reporter.storeInfo(location_data[store_number - 1])
                    choice5 = False
                else:
                    print("Please enter a valid number.")
            finally:
                input("Press Enter to continue...\n")
    elif choice == "6":
        reporter.locationInfo(location_data)
        input("Press Enter to continue...\n")
    elif choice == "7":
        choice7 = True
        while choice7:
            try:
                order_number = int(input('Choose a number (1-10): '))
                print('')
            except ValueError:
                print("Please enter a valid number.")
            else:
                if order_number >= 1 and order_number <= 10:
                    order_list[order_number - 1].resolve()
                    choice7 = False
                else:
                    print("Please enter a valid number.")
            finally:
                input("Press Enter to continue...\n")
    elif choice == "8":
        choice8 = True
        while choice8:
            try:
                order_number = int(input('Choose a number (1-10): '))
                print('')
            except ValueError:
                print("Please enter a valid number.")
            else:
                if order_number >= 1 and order_number <= 10:
                    order_list[order_number - 1].unresolve()
                    choice8 = False
                else:
                    print("Please enter a valid number.")
            finally:
                input("Press Enter to continue...\n")
    elif choice == "9":
        loop = False
    else:
        print("Please enter a valid option.")