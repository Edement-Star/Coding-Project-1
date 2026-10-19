# Change/Remove Data

def deleteVariableData(data: list, key, index):
    if key in data[index]:
        data[index].pop(key)
        return data
    return data

def insertDefault(data: list, key, index):
    if key in data[index]:
        if key == "Product" or key == "Provider":
            data[index][key] = "Unknown"
            return data
        elif key == 'Quantity':
            data[index][key] = "3"
            return data
        elif key == 'Unit Price':
            data[index][key] = "30.25"
            return data
    return data

def decide(data: list, key, index: int):
    if key == "Product" or key == "Provider" or key == "Quantity" or key == "Unit Price":
        #print('Replace')
        return insertDefault(data, key, index)
    elif key == 'Date Ordered' or key == 'Resolved':
        #print('Delete')
        return deleteVariableData(data, key, index)
    return data

def calculateTotalPrice(item):
        total = item.unit_price * item.quantity
        return total
def calculateFullTotalPrice(data: list):
    total = 0
    for item in range(len(data)):
        total += item.unit_price * item.quantity
    return total
