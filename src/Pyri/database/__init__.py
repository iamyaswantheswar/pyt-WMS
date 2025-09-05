from pathlib import Path

base_path = Path(__file__).parent.parent.parent.parent
product_path = base_path / 'data' / 'database' / 'inventory.csv'
vendor_path = base_path / 'data' / 'database' / 'vendors.csv'
sales_path = base_path / 'data' / 'database' / 'sales.csv'
purchase_path = base_path / 'data' / 'database' / 'purchases.csv'
location_path = base_path / 'data' / 'database' / 'locations.csv'
customer_path = base_path / 'data' / 'database' / 'customers.csv'


def check_inventory_csv():
    if Path(product_path).exists():
        return True
    else:
        return False

def check_vendor_csv():
    if Path(vendor_path).exists():
        return True
    else:
        return False

def check_sales_csv():
    if Path(sales_path).exists():
        return True
    else:
        return False

def check_purchase_csv():
    if Path(purchase_path).exists():
        return True
    else:
        return False

def check_location_csv():
    if Path(location_path).exists():
        return True
    else:
        return False

def check_customer_csv():
    if Path(customer_path).exists():
        return True
    else:
        return False