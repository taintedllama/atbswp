stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv = {'gold': 42, 'rope': 1}
dragonLoot ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print('Inventory:')
    itemTotal = 0
    for k, v in inventory.items():
        print('{} {}'.format(v, k))
        itemTotal += v
    print('Total number of items: {}'.format(itemTotal))

def addToInventory(inventory, addedItems):


displayInventory(stuff)