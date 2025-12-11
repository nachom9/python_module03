#!/usr/bin/env python3


def show_inventory(inventory: dict):

    for name, data in inventory.items():
        print(f"{name} {data['item']}")

def main():

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
    show_inventory(alice_inventory)


if __name__ == "__main__":
    main()
