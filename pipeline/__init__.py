# Core Information Here
# Purchase Order, 10 Data points; Primary Key: Int, Product: String, Provider: String,
# Quantity: Int, Unit Price: Float, Resolved?: Boolean, Date Ordered: Tuple (Str, Int, Int)
# Store Info, 3 Points; Primary Key: Int, Address: String, PhoneNum: String

# Data is AI Generate. For the purpose of being deliberately incorrect.
ORDERS = [
    {
        "Product": 12345,  # should be str
        "Quantity": 5,
        "Unit Price": 24.99,
        "Provider": "TechSupply Inc.",
        "Resolved": False
    },
    {
        "Product": "Mechanical Keyboard",
        "Quantity": "2",  # should be int
        "Unit Price": 89.50,
        "Provider": "OfficeGear Ltd.",
        "Date Ordered": ("February", 3, 2026),
        "Resolved": True
    },
    {
        "Product": "USB-C Hub",
        "Quantity": 10,
        "Unit Price": "15.75",  # should be float
        "Provider": "Connect Solutions",
        "Date Ordered": ("March", 22, 2026),
        "Resolved": False
    },
    {
        "Product": "27-inch Monitor",
        "Quantity": 3,
        "Unit Price": 199.99,
        "Provider": ["Display World"],  # should be str
        "Date Ordered": ("April", 8, 2026),
        "Resolved": True
    },
    {
        "Product": "Laptop Stand",
        "Quantity": [7],  # should be int
        "Unit Price": 34.95,
        "Provider": "Workspace Essentials",
        "Date Ordered": ("May", 17, 2026),
        "Resolved": False
    },
    {
        "Product": "Webcam",
        "Quantity": 4,
        "Unit Price": 59.99,
        "Provider": "Vision Tech",
        "Date Ordered": "June 12, 2026",  # should be tuple
        "Resolved": True
    },
    {
        "Product": "Ethernet Cable",
        "Quantity": 25,
        "Unit Price": 8.49,
        "Provider": "Network Supply Co.",
        "Date Ordered": ("July", 29, 2026),
        "Resolved": "False"  # should be bool
    },
    {
        "Product": "Desk Chair",
        "Quantity": None,  # should be int
        "Unit Price": 249.95,
        "Provider": "Comfort Furniture",
        "Date Ordered": ("August", 14, 2026),
        "Resolved": True
    },
    {
        "Product": "External SSD",
        "Quantity": 6,
        "Unit Price": False,  # should be float
        "Provider": "Storage Experts",
        "Date Ordered": ("September", 5, 2026),
        "Resolved": False
    },
    {
        "Product": "Printer Paper",
        "Quantity": 50,
        "Unit Price": 6.25,
        "Provider": "Office Supplies Plus",
        "Date Ordered": {"month": "October", "day": 11, "year": 2026},  # should be tuple
        "Resolved": 1  # should be bool
    }
]
STORES = [
    {
        "Address": "123 Maple Grove Drive, Springfield, NY 11701",
        "Phone": "(555) 123-4567"
    },
    {
        "Address": "456 Cedar Lane, Riverton, TX 75001",
        "Phone": "(555) 234-5678"
    },
    {
        "Address": "789 Oak Street, Lakeside, CA 92040",
        "Phone": "(555) 345-6789"
    }
]