# These are python library imports, more information would be
# available on the public API
import tkinter as tk
import time

# These are local imports from other files in your directory
# structure
from Character.character import Character
from Config.config import Config

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
    conf = Config("config.json")
    char_list = conf.get_char_list()
    print(char_list)

    main_char = char_list['main_char']
    main_char.level_up()
    main_char.pretty_print_stats()

    villain = char_list['example_villain']
    villain.level_up()
    villain.pretty_print_stats()
    
if __name__ == "__main__":
    main()