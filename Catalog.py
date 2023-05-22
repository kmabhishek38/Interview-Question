# Catalog
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount Rules
discount_rules = {
    "flat_10_discount": 10,
    "bulk_5_discount": 5,
    "bulk_10_discount": 10,
    "tiered_50_discount": 50
}

# Fees
gift_wrap_fee = 1
shipping_fee_per_package = 5
units_per_package = 10

# Prompt user for quantity and gift wrap status for each product
product_quantities = {}
for product, price in catalog.items():
    quantity = int(input(f"Enter the quantity of {product}: "))
    gift_wrap = input(f"Is {product} wrapped as a gift? (yes/no): ").lower() == "yes"
    product_quantities[product] = (quantity, price, gift_wrap)

# Calculate total quantity, cart total, and discount amount
total_quantity = sum(quantity for quantity, _, _ in product_quantities.values())
cart_total = sum(quantity * price for quantity, price, _ in product_quantities.values())

discount_amount = 0
discount_rule = ""
for rule, rule_discount in discount_rules.items():
    if rule == "flat_10_discount" and cart_total > 200:
        discount_amount = min(rule_discount, discount_amount)
    elif rule == "bulk_5_discount" and any(quantity > 10 for quantity, _, _ in product_quantities.values()):
        discount_amount = max(rule_discount, discount_amount)
        discount_rule = rule
    elif rule == "bulk_10_discount" and total_quantity > 20:
        discount_amount = max(rule_discount, discount_amount)
        discount_rule = rule
    elif rule == "tiered_50_discount" and total_quantity > 30 and any(quantity > 15 for quantity, _, _ in product_quantities.values()):
        discount_amount = max(rule_discount, discount_amount)
        discount_rule = rule

# Calculate shipping fee and gift wrap fee
total_units = sum(quantity for quantity, _, _ in product_quantities.values())
total_packages = (total_units + units_per_package - 1) // units_per_package
shipping_fee = total_packages * shipping_fee_per_package
gift_wrap_fee = sum(quantity * gift_wrap_fee for quantity, _, gift_wrap in product_quantities.values() if gift_wrap)

# Display details
print("Product Details:")
for product, (quantity, price, _) in product_quantities.items():
    product_amount = quantity * price
    print(f"{product} - Quantity: {quantity}, Total Amount: ${product_amount}")

print("----------")
print("Subtotal:", cart_total)
print("Discount Applied:", discount_rule)
print("Discount Amount:", discount_amount)
print("Shipping Fee:", shipping_fee)
print("Gift Wrap Fee:", gift_wrap_fee)
print("Total:", cart_total - discount_amount + shipping_fee + gift_wrap_fee)
