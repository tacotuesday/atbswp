def addToInventory(inventory, addedItems):
    for k in addedItems:
        if k not in inventory:
            inventory[k] = 1
        else:
            inventory[k] += 1
    return(inventory)

def displayInventory(currentInv):
        print('Inventory:')
        item_total = 0
        for a, b in currentInv.items():
            print(str(b) + ' ' + a)
            item_total = item_total + b
        print('Total number of items: ' + str(item_total))

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)