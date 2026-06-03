import json
import pathlib
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Source - https://codereview.stackexchange.com/q/222354
# Posted by Justin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-03-27, License - CC BY-SA 4.0

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'emerald', 'emerald', 'sapphire']

def display_inventory(inventory):
    print("Inventory:")
    item_total=0
    for k, v in inventory.items():
        print(f"{k}:{v}")
        item_total+=v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_stuff):
  
    for item in added_stuff:
        if item in inventory:
            inventory[item]+=1
        else: 
            inventory[item]=1
    display_inventory(inventory)
add_to_inventory(stuff, dragon_loot)
