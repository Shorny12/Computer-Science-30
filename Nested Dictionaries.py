# RPG Nested Dictionaries
# Zhixiang Wang
# CS 30 AM class
# Date Created: Janaury 29, 2021
# Date Modified: Janaury 29, 2021

# Dictionary for character
print("characters:\n")
characters = {
    # The Hero description
    "hero": {
        "description": "The player who is trying to find the treasure",
        "health": 100,
        "damage": 5,
    },
    # The guards description
    "guards": {
        "description": "The guard who have the keys to the treasure room",
        "health": 150,
        "damage": 20,
    },
    # The prisoner description
    "prisoner": {
        "description": "The prisoner who is in the jail",
        "health": 10,
        "damage": 0,
    },
    # The devil description
    "devil": {
        "description": "The boss in the castle",
        "health": 300,
        "damage": 50,
    },
    # The cook description
    "cook": {
        "description": "The cook, beat him to get some food",
        "health": 50,
        "damage": 10,
    },
    # The giant spider description
    "giant Spider": {
        "description": "A small monster in the castle",
        "health": 70,
        "damage": 15,
    },
    # The giant rat description
    "giant Rat": {
        "description": "A small monster in the jail",
        "health": 70,
        "damage": 15,
    },
    # The witch description
    "witch": {
      "description": "A small monster in the lab",
      "health": 60,
      "damage": 40,
    }
}

# Loop For characters
for character, traits in characters.items():
    print(f"#{character.title()}:")
    print(f"{character.title()} is {traits['description']}:")
    print(f"{character.title()}'s health is {traits['health']}:")
    print(f"{character.title()}'s damage is {traits['damage']}:")
    print("")

# Use a line to seperate the first dictionary and second dictionary
print("____________________________________________________")
print("")

# Dictionary for inventory
print("Item in inventory:\n")
inventory = {
    # Sword description
    "sword": {
        "description": "A very sharp sword",
        "amount": 1,
        "damage": 25,
        "health": 0,
        "health restore": 0,
    },
    # Armour description
    "armour": {
       "description": "A heavy armour",
       "amount": 1,
       "damage": 0,
       "health": 70,
       "health restore": 0,
    },
    # Map description
    "map": {
        "description": "A map of the castle",
        "amount": 1,
        "damage": 0,
        "health": 0,
        "health restore": 0,
    },
    # Bondage description
    "bondage": {
        "description": "A bondage that can heal you",
        "amount": 1,
        "damage": 0,
        "health": 0,
        "health restore": 90,
    },
    # Pizza description
    "pizza": {
        "description": "A huge slice of pizza",
        "amount": 1,
        "damage": 0,
        "health": 0,
        "health restore": 20,
    },
    # glass bottle description
    "glass bottle": {
        "description": "An empty glass bottle ",
        "amount": 1,
        "damage": 0,
        "health": 0,
        "health restore": 0,
    },
    # Key description
    "key": {
        "description": "A key to open the door",
        "amount": 1,
        "damage": 0,
        "health": 0,
        "health restore": 0,
    },
    # Hammer description
    "hammer": {
        "description": "A heavy hammer",
        "amount": 1,
        "damage": 90,
        "health": 0,
        "health restore": 0,
    },
    # Poison plant description
    "poison plant": {
        "description": "A poison plant",
        "amount": 1,
        "damage": 10,
        "health": 0,
        "health restore": 0,
    },
    # Spider venom description
    "spider venom plant": {
        "description": "The venom of the giant spider",
        "amount": 1,
        "damage": 10,
        "health": 0,
        "health restore": 0,
    },
    # Poison bomb description
    " poison": {
        "description": "A bomb made with venom and poison plant",
        "amount": 1,
        "damage": 200,
        "health": 0,
        "health restore": 0,
    },
    # Treasure description
    " treasure": {
        "description": "The treasure in the castle",
        "amount": 1000000000000000,
        "damage": 0,
        "health": 0,
        "health restore": 0,
    },
}

# Loop For Inventory
for inventory, traits in inventory.items():
    print(f"#{inventory.title()}:")
    for info, descript in traits.items():
        print(f"{info.title()}: {descript}")
    print("")

# Use a line to seperate the second dictionary and third dictionary
print("____________________________________________________")
print("")

# Dictionary for Locations
print("locations:\n")
locations = {
    # Jail
    "jail": [
        "where the prisoner is kepted",
        "where the giant rat is at",
        "on the lower floor",
    ],
    # Kitchen
    "kitchen": [
        "where the cook is at",
        "where the pizza is at",
        "on the main floor",
    ],
    # Lab
    "lab": [
        "where the glass bottle is kepted",
        "where the witch is at",
        "on the lower floor",
    ],
    # Blacksmith shop
    "blacksmith shop": [
        "where the hammer is at",
        "on the main floor",
    ],
    #  Hallway
    "hallway": [
        "where the giant spider is at",
        "between main floor and second floor",
    ],
    # Staircase
    "staircase": [
        "where the guard is at",
        "where the key is at",
        "on the main floor",
    ],
    # Front door
    "front door": [
        "where the map is at",
        "on the main floor",
    ],
    # Treasure room
    "treasure room": [
        "where the devil is at",
        "where the treasure is at",
        "on the second floor",
    ],
}

# Loop for locations
# Loop the dictionary, locations and print its keps and values seperately
for location, descriptions in locations.items():
    msg = f"{location.title()} is the place "
    for i, description in enumerate(descriptions):
        msg += description
        # put a . after the last sentence
        if i == len(descriptions) - 1:
            msg += "."
        # put an and after the second last sentence
        elif i == len(descriptions) - 2:
            msg += ", and "
        # put , before every sentence that is not the last or second last
        else:
            msg += ", "
    print(msg)
    print("")
