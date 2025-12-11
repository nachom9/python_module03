#!/usr/bin/env python3

class AchTrackerSystem:

    unique_achs = set()
    common_achs = set()
    rare_achs = set()
    all_players = []


    def __init__(self, name, achs):
        self.name = name
        self.achs = achs

    @classmethod
    def create_list_player(cls, players: list):

        cls.all_players = players

    @classmethod
    def set_achs(cls) -> None:

        print("=== Achievement Tracker System ===\n")
        for player in cls.all_players:
            print(f"Player {player.name} achievement:", player.achs)

    @classmethod
    def unique_ach(cls):

        print("=== Achievement Analytics ===")
        for player in cls.all_players:
            cls.unique_achs |= player.achs
        print("All unique achievements:", cls.unique_achs)
        print("Total unique achievements:", len(cls.unique_achs))

    @classmethod
    def common_ach(cls):

        for player in cls.all_players:
            if not cls.common_achs:
                cls.common_achs = player.achs
            else:
                cls.common_achs = cls.common_achs.intersection(player.achs)
        print("Common to all players:", cls.common_achs)

    @classmethod
    def rare_ach(cls):
        for achievement in cls.unique_achs:
            count = 0
            for player in cls.all_players:
                for ach in player.achs:
                    if ach == achievement:
                        count += 1
            if count == 1:
                cls.rare_achs.add(achievement)
        print("Rare achievements (1 player):", cls.rare_achs)

    @staticmethod
    def compare_players(player1, player2):
        common = player1.achs.intersection(player2.achs)
        player1_unique = player1.achs.difference(player2.achs)
        player2_unique = player2.achs.difference(player1.achs)
        print(f"{player1.name} vs {player2.name} common:", common)
        print(f"{player1.name} unique:", player1_unique)
        print(f"{player2.name} unique:", player2_unique)


def main():

    alice = AchTrackerSystem("Alice", {'first_kill', 'level_10',
                                       'treasure_hunter', 'speed_demon'})
    bob = AchTrackerSystem("Bob", {'first_kill', 'level_10',
                                   'boss_slayer', 'collector'})
    charlie = AchTrackerSystem("Charlie", {'level_10', 'treasure_hunter',
                                           'boss_slayer', 'speed_demon',
                                           'perfectionist'})
    AchTrackerSystem.create_list_player([alice, bob, charlie])
    AchTrackerSystem.set_achs()
    print("")
    AchTrackerSystem.unique_ach()
    print("")
    AchTrackerSystem.common_ach()
    AchTrackerSystem.rare_ach()
    print("")
    AchTrackerSystem.compare_players(alice, bob)


if __name__ == "__main__":

    main()
