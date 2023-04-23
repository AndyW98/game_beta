from src.UI.game import GameState, UserInterface
from src.Config.config import Config
from src.Item.Weapon.stick import Stick
from src.Item.Weapon.knife import Knife

import pytest

def test_game():
    # gs = GameState()

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

    ui = UserInterface()


    assert(True)

if __name__ == "__main__":
    test_game()