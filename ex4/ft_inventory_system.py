#!/usr/bin/env python3

def get_data():

    data = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1, 'code_bow': 1,
                    'health_byte': 1, 'quantum_ring': 3
                },
                'total_value': 1875, 'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3, 'pixel_sword': 2
                },
                'total_value': 900, 'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1, 'code_bow': 1
                },
                'total_value': 350, 'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3, 'pixel_sword': 3,
                    'health_byte': 3, 'data_crystal': 3
                },
                'total_value': 4125, 'item_count': 12
                }
        },
        'catalog': {
            'pixel_sword': {
                'type': 'weapon', 'value': 150, 'rarity': 'common'
            },
            'quantum_ring': {
                'type': 'accessory', 'value': 500, 'rarity': 'rare'
            },
            'health_byte': {
                'type': 'consumable', 'value': 25, 'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material', 'value': 1000, 'rarity': 'legendary'
            },
            'code_bow': {
                'type': 'weapon', 'value': 200, 'rarity': 'uncommon'
            }
        }
    }

    return data


class Inventory:

    def show_inventory(data: dict, player: str):

        categories = {}
        print_categories = "Categories: "
        players = data['players']
        catalog = data['catalog']
        inventory = players[player]['items']
        for name, amount in inventory.items():
            item_type = catalog[name]['type']
            rarity = catalog[name]['rarity']
            try:
                categories[item_type] += amount
            except KeyError:
                categories[item_type] = amount
            value = catalog[name]['value']
            print(f"{name} ({item_type}, {rarity}): {amount}x @ {value} "
                  f"gold each = {value * amount}")

        print(f"\nInventory value: {players[player]['total_value']} gold")
        print(f"Item count: {players[player]['item_count']} items")
        for category, number in categories.items():
            print_categories += f"{category}({number}), "
        print(print_categories[:-2])

    def transaction(data: dict, gives: str, recieves: str, amount: int,
                    item: str):

        players = data['players']
        gives_has = players[gives]['items'].get(item, 0)
        recieves_has = players[recieves]['items'].get(item, 0)
        item_value = data['catalog'][item]['value']

        if gives_has < amount:
            print(f"Error. {gives} can't give {amount} {item}, they only "
                  f"have {gives_has}")
            return
        if amount <= 0:
            print("Error. Cant give 0 or less of an item")
            return

        players[gives]['items'][item] -= amount

        if recieves_has == 0:
            players[recieves]['items'][item] = amount
        elif recieves_has > 0:
            players[recieves]['items'][item] += amount

        new_inventory = {}
        if players[gives]['items'].get(item, 0) == 0:
            for name, data in players[gives]['items'].items():
                if name != item:
                    new_inventory[name] = data
            players[gives]['items'] = new_inventory

        players[gives]['total_value'] -= amount * item_value
        players[recieves]['total_value'] += amount * item_value
        players[gives]['item_count'] -= amount
        players[recieves]['item_count'] += amount

        if amount == 1:
            print(f"=== Transaction: {gives} gives {recieves} {amount} "
                  f"{item} ===")
        if amount > 1:
            print(f"=== Transaction: {gives} gives {recieves} {amount} "
                  f"{item}s ===")
        print("Transaction successful!")

        print("\n== Updated Inventories ===")
        print(f"{gives} {item}: {players[gives]['items'].get(item, 0)}")
        print(f"{recieves} {item}: {players[recieves]['items'].get(item, 0)}")

    def inventory_analytics(data: dict):

        max_value = 0
        players = data['players']
        catalog = data['catalog']

        categories_tier = {
            'common': 1,
            'uncommon': 2,
            'rare': 3,
            'legendary': 4
        }
        rarest_tier_count = 0
        for player in players:
            for item in players[player]['items']:
                rarity = catalog[item]['rarity']
                if categories_tier[rarity] > rarest_tier_count:
                    rarest_tier_count = categories_tier[rarity]
                    rarest_tier = rarity

        for player in players:
            if players[player]['total_value'] > max_value:
                max_value = players[player]['total_value']
                most_valuable = player
        print(f"Most valuable player: {most_valuable} ({max_value} gold)")

        max_items = 0
        for player in players:
            if players[player]['item_count'] > max_items:
                max_items = players[player]['item_count']
                most_items = player
        print(f"Most items: {most_items} ({max_items} items)")

        print_rarest_items = "rarest items: "
        for player in players:
            for item in players[player]['items']:
                if catalog[item]['rarity'] == rarest_tier:
                    print_rarest_items += f"{item}, "
        print(print_rarest_items[:-2])


def main():

    data = get_data()

    print("=== Player Inventory System ===")
    print("\n=== Alice's Inventory ===")
    Inventory.show_inventory(data, 'alice')
    print("")
    Inventory.transaction(data, 'alice', 'bob', 2, 'quantum_ring')
    print("\n=== Updated Inventories ===")
    Inventory.inventory_analytics(data)


if __name__ == "__main__":
    main()
