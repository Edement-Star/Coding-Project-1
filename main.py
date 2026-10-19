from pipeline import *
from pipeline import __init__
from pipeline import schema
from pipeline import validator
from pipeline import transformer
from pipeline import reporter

order_data = validator.correctData(ORDERS)
for i in range(len(order_data)):
    print(order_data[i]["Unit Price"])
    #new_order = schema.Order(i+1, order_data[i]["Product"], order_data[i]["Unit Price"], order_data[i]["Quantity"],
                             #order_data[i]["Provider"], order_data[i]["Date Ordered"], order_data[i]["Resolved"])
