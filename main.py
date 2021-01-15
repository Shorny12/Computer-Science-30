# RPG Inventory using lists
# Zhixiang Wang
# CS 30
# Date Modified: Janaury 14, 2021

# First list (weapons)
weapons = ['short Sword', 'armor']

# Second list (items)
items = ['letter', 'bandage', 'water bottle']

# Print items
print_items = (f"You have {items} in your backpack.")
print(print_items)
print ("")

# Print Weapons
print_weapons = (f"You are equipped with {weapons}.")
print(print_weapons)
print ("")

# Append a pizza
print('\n'*1)
items.append('pizza')
print(items)
supply = f"\nYou find a {items[3]} in the kitchen."
print(supply)

# Insert a hammer
print('\n'*1)
items.insert(2, 'hammer')
print(items)
discovery = f"\nYou find a giant {items[2]} and put it in your bag."
print(discovery)

# Del the bandage
print('\n'*1)
print (f"You used the {items[1]}.")
print("")
del items[1]
print_items = (f"You now have {items} in your backpack.")
print (print_items)
print ("")

# Pop equip the hammer
print('\n'*1)
equipped_hammer = items.pop(1)
print(f"You grab out your {equipped_hammer} from your backpack.")
print ("")

# Remove pizza
print('\n'*1)
message = f"\nYou ate the {items[2]}."
print(message)
items.remove('pizza')
print("")
print(f"Now you have {items} left in your backpack")

# Sort items
print('\n'*1)
items.sort()
print(f"\nThe items in the backpack are:\n\t{items}.")

# Lenth
print('\n'*1)
print(f"\t There are now {len(items)} items left in your backpack.")

# Third list (rooms)
print('\n'*1)
rooms = ['lobby', 'hallway', 'blacksmith shop', 'living room']

# Sorted rooms
print('\n'*1)
print("The original list:")
print(rooms)
print("\nThe sorted list:")
print(sorted(rooms))

# Reverse the order of rooms
print('\n'*1)
items.reverse()
print(f"\nThe reverse rooms:\n {rooms}.")
