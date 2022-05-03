# These are python library imports, more information would be
# available on the public API
import tkinter as tk
import time

# These are local imports from other files in your directory
# structure
from Character.character import Character
from Config.config import Config
from Combat.combat import Combat

from Item.item import Item
from Item.Weapon.weapon import Weapon
from Item.Weapon.stick import Stick
from Item.Weapon.knife import Knife

from UI.game import GameState, UserInterface
from UI.ScreenTypes.menu import *

'''
When making a large project, the first step you want to do is
break it down into smaller components. For example, if you want
to make a main character with an inventory, you can break it
down as follows:

1) A character object with variables such as name, health, etc.
2) An inventory object specific to the character
    a) Determine data structure for the inventory based
    on various factors such as size and what goes in it
    b) Have accessors to both add and remove items in
    the inventory
    c) Quickly display inventory items
        i) UI design
        ii) What relevant information will be displayed?
3) Art for the character that is used in the display window

This ends up being easily translatable to code, since you can
portion off each individual point to sections of code, as
well as having documentation for anybody that reads it.
'''
def main():
    
    # For now the main character can be defined in the main
    # function, but later on it's wiser to partition off its
    # declaration. Here, we make a main character with the
    # name of MAIN_CHAR_NAME
    conf = Config()
    char_list = conf.get_char_list()
    weapon_list = conf.get_data().get("items").get("weapons")
    game_info = conf.get_data().get('display').get('game_info')

    # Test items
    item_list = {}

    wood_spoon = Stick(weight=weapon_list.get("stick").get("weight"),
                       power=weapon_list.get("stick").get("damage"),
                       level=5,
                       name="Wood Spoon")
    item_list[wood_spoon.name] = wood_spoon

    kitchen_knife = Knife(weight=weapon_list.get("knife").get("weight"),
                          power=weapon_list.get("knife").get("damage"),
                          level=3,
                          name="Kitchen Knife")
    item_list[kitchen_knife.name] = kitchen_knife

    """main_char = char_list['main_char']
    main_char.level_up("str", "dex")

    # testing adding a weapon
    main_char.add_item(wood_spoon)
    main_char.equip_weapon(wood_spoon)

    villain = char_list['example_villain']
    villain.level_up("str", "dex")

    #Combat("melee", [main_char, villain])
    #main_char.pretty_print_stats()
    #villain.pretty_print_stats()

    main_char.attack(villain)
    main_char.attack(wood_spoon)
    print(main_char)
    print(villain)"""

    # Test for loading the menu
    #Menu(game_info).run()
    UserInterface(item_list, char_list, game_info).run()

    # Test for loading movement
    #Game(game_info).run()


    # Test print weapons
    # wood_spoon.print_weapon_stats()

if __name__ == "__main__":
    main()