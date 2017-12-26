def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory.keys():
            inventory[k] = 1
        else:
            inventory[k] += 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
# displayInventory(inv)