#!/usr/bin/env python3

def show_inventory(inventory: dict):

    for name, data in inventory.items():
        print(f"{name} ({data['item']}, {data['rarity']}): {data['amount']}"
              f" @ {data['cost']} gold each = {data['amount'] * data['cost']}"
              f" gold")

    total_value = 0
    total_items = 0
    weapon_count = 0
    consumable_count = 0
    armor_count = 0

    for value in inventory.values():
        total_value += value['amount'] * value['cost']
        total_items += value['amount']
        if value['item'] == "weapon":
            weapon_count += value['amount']
        elif value['item'] == "consumable":
            consumable_count += value['amount']
        elif value['item'] == "armor":
            armor_count += value['amount']

    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: weapon({weapon_count}), consumable({consumable_count})"
          f", armor({armor_count})")


def transaction(inventories: dict, gives: str, recieves: str, item_given: str,
                number: int) -> dict:

    has_item = False
    new_inventories = {
            "Alice": {},
            "Bob": dict(inventories[recieves]),
            }

    try:
        if inventories[gives][item_given]['amount'] < number:
            print(f"Error. Can't give {number} {item_given} to {recieves},"
                  f" {gives}"
                  f" has only {inventories[gives][item_given]['amount']}")
            return
    except KeyError:
        print(f"Error. {gives} has no {item_given}")
        return

    for name, data in inventories[recieves].items():
        if name == item_given:
            new_data = dict(data)
            new_data['amount'] += number
            new_inventories[recieves][name] = new_data
            has_item = True
        else:
            new_inventories[recieves][name] = dict(data)
    if has_item is False:
        new_inventories[recieves][item_given] = inventories[gives][item_given]
        new_inventories[recieves][item_given]['amount'] = number

    for name, data in inventories[gives].items():
        if name == item_given:
            if inventories[gives][item_given]['amount'] > number:
                new_data = dict(data)
                new_data['amount'] -= number
                new_inventories[gives][name] = new_data
        else:
            new_inventories[gives][name] = dict(data)

    return new_inventories


def inventory_analytics(inventories: dict) -> None:

    max_items = 0
    max_value = 0
    saved_name = ""
    rarest_items = {}

    for player in inventories:
        tmp_max_value = 0
        for name, data in inventories[player].items():
            tmp_max_value += data['cost'] * data['amount']
            if data['rarity'] == "rare":
                rarest_items[name] = dict(data)
        if tmp_max_value > max_value:
            max_value = tmp_max_value
            saved_name = player
    print(f"Most valuable player: {saved_name} ({max_value})")

    for player in inventories:
        tmp_max_items = 0
        for name, data in inventories[player].items():
            tmp_max_items += data['amount']
        if tmp_max_items > max_items:
            max_items = tmp_max_items
            saved_name = player

    print(f"Most items: {saved_name} ({max_items} items)")

    print("Rarest items:", end=" ")
    first = True
    for name in rarest_items.keys():
        if not first:
            print(", ", end="")
        print(name)
        print("", end="")
        first = False


def main():

    print("=== Player Inventory System ===")
    print("")

    new_inventories = None
    alice_inventory = {
            "sword": {
                "item": "weapon",
                "rarity": "rare",
                "amount": 1,
                "cost": 500,
                },
            "potion": {
                "item": "consumable",
                "rarity": "common",
                "amount": 2,
                "cost": 50,
                },
            "shield": {
                "item": "armor",
                "rarity": "uncommon",
                "amount": 1,
                "cost": 200,
                }
            }

    bob_inventory = {
            "sword": {
                "item": "weapon",
                "rarity": "rare",
                "amount": 1,
                "cost": 500,
                },
            "potion": {
                "item": "consumable",
                "rarity": "common",
                "amount": 2,
                "cost": 50,
                },
            "shield": {
                "item": "armor",
                "rarity": "uncommon",
                "amount": 1,
                "cost": 200,
                }
            }
    inventories = {
            "Alice": alice_inventory,
            "Bob": bob_inventory}

    print("=== Alice's Inventory ===")
    show_inventory(alice_inventory)
    print("")

    print("=== Transaction: Alice gives Bob 2 potions ===")
    new_inventories = transaction(inventories, "Alice", "Bob", "potion", 2)
    if new_inventories:
        inventories.update(new_inventories)
        print("Transaction successful!")
        print("\n=== Updated Inventories ===")
        try:
            print(f"Alice potions: {inventories['Alice']['potion']['amount']}")
        except KeyError:
            print("Alice potions: 0")
        print(f"Bob potions: {inventories['Bob']['potion']['amount']}")
    else:
        print("Transaction failed!")
    print("")

    print("=== Inventory Analytics ===")
    inventory_analytics(inventories)


if __name__ == "__main__":
    main()
