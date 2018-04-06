inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        itemTotal += v
    print('Total number of items: {}'.format(itemTotal))

def addToInventory(inventory, addedItems):
    for k in range(len(addedItems)):
        if addedItems[k] in inventory.keys():
            inventory[addedItems[k]] += 1
        else:
            inventory.setdefault(addedItems[k], 1)
    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)