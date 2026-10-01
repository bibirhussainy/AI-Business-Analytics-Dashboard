import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Technology", 1200, 850),
    "Monitor": ("Technology", 350, 220),
    "Keyboard": ("Accessories", 80, 35),
    "Mouse": ("Accessories", 45, 18),
    "Headphones": ("Accessories", 120, 55),
    "Office Chair": ("Furniture", 300, 190),
    "Desk": ("Furniture", 450, 280),
    "Printer": ("Technology", 250, 160),
}

regions = ["Dublin", "Cork", "Galway", "Limerick"]
customer_types = ["New Customer", "Returning Customer"]

data = []

start_date = datetime(2025, 1, 1)

for i in range(1000):

    date = start_date + timedelta(days=random.randint(0, 364))

    product = random.choice(list(products.keys()))

    category, price, unit_cost = products[product]

    quantity = random.randint(1, 8)

    region = random.choice(regions)

    customer_type = random.choice(customer_types)

    sales = price * quantity
    cost = unit_cost * quantity
    profit = sales - cost

    data.append({
        "Date": date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Region": region,
        "Customer Type": customer_type,
        "Quantity": quantity,
        "Sales": sales,
        "Cost": cost,
        "Profit": profit
    })

df = pd.DataFrame(data)

df = df.sort_values("Date")

df.to_csv("sales_data.csv", index=False)

print("sales_data.csv created successfully!")
print(f"Rows: {len(df)}")