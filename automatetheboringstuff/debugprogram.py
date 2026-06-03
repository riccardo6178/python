
def display_inventory(inventory: dict):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f'{k} {v}')
        item_total+=v
    print("Total number of items: " + str(item_total))


def add_to_inventory(inventory, added_items):
    for i in added_items:
        if inventory.get(i):
            inventory[i]+=1
        else:
            inventory[i]=1
    return inventory





inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)

