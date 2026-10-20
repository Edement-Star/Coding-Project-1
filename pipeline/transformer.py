# Change/Remove Data

def deleteVariableData(data: list, key, index):
    if key in data[index]:
        data[index].pop(key)
    return data

def insertDefault(data: list, key, index):
    if key in data[index]:
        if key == "Product" or key == "Provider":
            try:
                data[index][key] = data[index][key][0]
            except TypeError:
                data[index][key] = "Unknown"
        elif key == 'Quantity':
            if not data[index][key]:
                data[index][key] = 3
            else:
                try:
                    data[index][key] = int(data[index][key])
                except TypeError:
                    data[index][key] = int(data[index][key][0])
        elif key == 'Unit Price':
            if not data[index][key]:
                data[index][key] = 30.25
            else:
                try:
                    data[index][key] = float(data[index][key])
                except TypeError:
                    data[index][key] = float(data[index][key][0])
    return data

def decide(data: list, key, index: int):
    if key == "Product" or key == "Provider" or key == "Quantity" or key == "Unit Price":
        #print('Replace')
        data = insertDefault(data, key, index)
    elif key == 'Date Ordered' or key == 'Resolved':
        #print('Delete')
        data = deleteVariableData(data, key, index)
    return data

def calculateTotalPrice(item):
        total = item.unit_price * float(item.quantity)
        return total
def calculateFullTotalPrice(data: list):
    total = 0
    for item in data:
        total += item.unit_price * float(item.quantity)
    return total
