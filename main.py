from discount import final_price, TAX_RATE

# Confirm TAX_RATE imported correctly
print(f"TAX_RATE imported from discount.py: {TAX_RATE} ({int(TAX_RATE * 100)}% VAT)")
print()

# Given data
products = [
    ("Laptop",     85000, 10),
    ("Headphones",  4500, 15),
    ("Phone Case",   800,  5),
    ("USB Cable",    600,  0),
]

# Print shopping summary
print("=" * 55)
print("          Nepal Shopping - Discount & Tax Summary")
print("=" * 55)
print(f"  {'Product':<15} {'Original (NPR)':>15} {'Final (NPR)':>15}")
print("-" * 55)

for name, price, discount in products:
    fp = final_price(price, discount)
    print(f"  {name:<15} {price:>15,.2f} {fp:>15,.2f}")

print("=" * 55)
print(f"  All prices include {int(TAX_RATE * 100)}% VAT after discount.")
print("=" * 55)
