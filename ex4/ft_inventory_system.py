#!/usr/bin/env python3


def show_inventory(inventory: dict):

    for name, data in inventory.items():
        print(f"{name} ({data['item']}, {data['rarity']}): {data['amount']}"
              f" @ {data['cost']} gold each = {data['amount'] * data['cost']} gold")

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

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_items} items")
    print(f"Categories: weapon({weapon_count}), consumable({consumable_count})"
          f", armor({armor_count})")


def transaction(inventory1: dict, inventory2: dict, item: str, number: int):


    new_inventory = {}

    for name, data in inventory1.items():
        if name == item and data['amount'] < number:
            print("Not enough amount")
            return
    for name, data in inventory1.items():
        if name == item:
            if data['amount'] > number:
                new_data = dict(data)
                new_data['amount'] -= number
                new_inventory[name] = new_data
        else:
            new_inventory[name] = dict(data)

    inventory1.update(new_inventory)
                

def main():

    print("=== Player Inventory System ===")
    print("")
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
                "amount": 5,
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
            "shield": {
                "item": "armor",
                "rarity": "uncommon",
                "amount": 1,
                "cost": 200,
                }
            }

    print("=== Alice's Inventory ===")
    show_inventory(alice_inventory)
    print("")
    print("=== Transaction: Alice gives Bob 2 potions ===")
    transaction(alice_inventory, bob_inventory, "potion", 5)
    show_inventory(alice_inventory)


if __name__ == "__main__":
    main()
