import sys

print("=== Inventory System Analysis ===")

inventory = {}

for arg in sys.argv[1:]:
    if ":" not in arg:
        print(f"Error - invalid parameter '{arg}'")
        continue

    name, quantity = arg.split(":", 1)

    if name in inventory:
        print(f"Redundant item '{name}' - discarding")
        continue

    try:
        quantity = int(quantity)
    except ValueError as e:
        print(f"Quantity error for '{name}': {e}")
        continue

    inventory[name] = quantity

print(f"Got inventory: {inventory}")
print(f"Item list: {list(inventory.keys())}")
total = sum(inventory.values())
print(f"Total quantity of the {len(inventory)} items: {total}")
for name in inventory:
    quantity = inventory[name]
    if total == 0:
        percent = 0
    else:
        percent = round((quantity / total) * 100, 1)
    print(f"Item {name} represents {percent}%")
