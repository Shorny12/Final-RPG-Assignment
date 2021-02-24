# Classes
# Zhixiang Wang
# CS 30 AM class
# Date Created: February 20, 2021
# Date Modified: February 24, 2021

import map
import sys
import items
import enemies


def info():
    while True:
        print("""
Choose one of the following actions:
- q: Quit
- m: Map
- i: Items
- e: Enemies
        """)
        action = input('Action:').lower()
        if action in ['q', 'quit']:
            print('Exit the demo!')
            sys.exit()
        elif action in ['m', 'map']:
            # Show map string
            # print(map.room_dsl)
            # Read the map string and update the map list
            map.parse_room_dsl()
            # # Display the map in the game
            if isinstance(map.room_map[1][1], map.StartRoom):
                map.room_map[1][1].print_map()
        elif action in ['i', 'items']:
            print('Weapon:')
            print(items.Guns())
            print(items.Bullet())
            print('Consumable:')
            print(items.Soup())
            print(items.Poison())
            print('Keys:')
            print(items.KeyToAuditorium())
            print(items.KeyToLibrary())
        elif action in ['e', 'enemies']:
            print('Enemies:')
            print(enemies.Monster())
            print(enemies.Keeper())
        else:
            print("Invalid action!")

info()
