# Module and Map
# Zhixiang Wang
# CS 30 AM class
# Date Created: February 5, 2021
# Date Modified: February 7, 2021

import random
from tabulate import tabulate


def append_list(dictionary, list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)


def replace_tile(list, tile1, tile2):
    """Make sure that replaced tiles do not overwrite each other"""
    while random_tile(list, tile1) == random_tile(list, tile2):
            random_tile(list, tile1)
            random_tile(list, tile2)


def random_tile(list, tile):
    """Choose a random tile to replace and return the indices"""
    x = random.choice(list)
    y = random.choice(x)
    n = list.index(x)
    m = x.index(y)
    list[n][m] = tile
    return (n, m)


def generate_map(list):
    """randomly generate a 3x3 room tile types"""
    map = [[random.choice(list) for i in range(3)] for j in range(3)]
    # add boss and start tiles
    replace_tile(map, "Devil", "Start")
    return map


def print_map(dictionary):
    """print out each room generated"""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        # format the maps in rows and columns
        print(tabulate(map, tablefmt="plain"))
        print("\n")


# Room tiles
rooms = {"Treasure room": "Where the Devil and the treasure are at",
         "Stairway": "Stairway to Treasure room",
         "Lab": "Where the witch is at",
         "Blacksmith shop": "Has the item hammer",
         "Kitchen": "Where the cook is at",
         "Jail": "Where the prisoner is at",
         "Hallway": "Where the giant spider is at",
         "Empty Room": "There is nothing here",
         "Balcony": "There is nothing here"
         }
# map tile types
map_tiles = {"Enemy": {"description":
                       "location of an enemy",
                       "abbreviation": "ET",
                       "action": "must defeat the enemy to continue"},
             "Devil": {"description":
                       "The Boss of the castle",
                       "abbreviation": "DT",
                       "action":
                       "Have to fight the devil to win"},
             "Weapons": {"description":
                         "location of a weapon",
                         "abbreviation": "WT",
                         "action":
                         "may pick up weapon or move to another location"},
             "Supplies": {"description":
                          "location of protection and healing items",
                          "abbreviation": "ST",
                          "action": "must pick up the item to continue"},
             " ": {"description":
                   "tile with nothing",
                   "abbreviation": "BT",
                   "action": "may rest or move to another location"},
             "Start": {"description":
                       "entrance to the castle",
                       "abbreviation": "S",
                       "action": "may rest or move to another location"}
             }

# generate a list of cities
castle_level = []
append_list(rooms, castle_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Devil")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for castle in castle_level:
    castle_map = generate_map(tile_types)
    main_map[castle] = castle_map

# print_map(main_map)
