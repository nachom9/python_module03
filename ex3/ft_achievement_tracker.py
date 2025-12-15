#!/usr/bin/env python3

class AchTrackerSystem:

    unique_achs = set()
    common_achs = set()
    rare_achs = set()

    @staticmethod
    def set_achs(players) -> None:
        print("=== Achievement Tracker System ===\n")
        for player in players:
            print(f"Player {player} achievements: {set(players[player])}")

    @classmethod
    def ach_analytics(cls, players) -> None:
        print("=== Achievement Analytics ===")

        for player in players:
            cls.unique_achs = set(players[player]).union(cls.unique_achs)
        if len(cls.unique_achs) > 0:
            print(f"All unique achievements: {cls.unique_achs}")
            print(f"Total unique achievements: {len(cls.unique_achs)}")
        else:
            print("There are no unique achievements")

    @classmethod
    def advanced_analytics(cls, players) -> None:
        first = True
        for player in players:
            if first is True:
                cls.common_achs = set(players[player])
                first = False
            else:
                tmp_common_achs = (
                    set(players[player]).intersection(cls.common_achs)
                )
                cls.common_achs = tmp_common_achs
            tmp_common_achs = set()
        if len(cls.common_achs) > 0:
            print(f"Common to all players: {cls.common_achs}")
        else:
            print("There are no common achievements")

        for unique_ach in cls.unique_achs:
            player_count = 0
            for player in players:
                player_has_ach = False
                for ach in players[player]:
                    if ach == unique_ach:
                        player_has_ach = True
                if player_has_ach:
                    player_count += 1
            if player_count == 1:
                cls.rare_achs = set(cls.rare_achs).union([unique_ach])
        if len(cls.rare_achs) > 0:
            print(f"Rare achievements (1 player): {cls.rare_achs}")
        else:
            print("There are no rare achievements")

    @classmethod
    def ach_comparision(cls, player1, player2, players):

        common_achievements = (
            set(players[player1]).intersection(players[player2])
        )
        if len(common_achievements) > 0:
            print(f"{player1} vs {player2} common: {common_achievements}")
        else:
            print(f"There are no common achievements between "
                  f"{player1} and {player2}")

        player1_unique = set(players[player1]).difference(players[player2])
        if len(player1_unique) > 0:
            print(f"{player1} unique: {player1_unique}")
        else:
            print(f"{player1} has no unique achievements")

        player2_unique = set(players[player2]).difference(players[player1])
        if len(player2_unique) > 0:
            print(f"{player2} unique: {player2_unique}")
        else:
            print(f"{player2} has no unique achievements")


def main():

    players = {'alice': ['first_blood', 'pixel_perfect', 'speed_runner',
                         'first_blood', 'first_blood'],
               'bob': ['level_master', 'boss_hunter', 'treasure_seeker',
                       'level_master', 'level_master'],
               'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king',
                           'first_blood', 'boss_hunter', 'first_blood',
                           'boss_hunter', 'first_blood'],
               'diana': ['first_blood', 'combo_king', 'level_master',
                         'treasure_seeker', 'speed_runner', 'combo_king',
                         'combo_king', 'level_master'],
               'eve': ['level_master', 'treasure_seeker', 'first_blood',
                       'treasure_seeker', 'first_blood', 'treasure_seeker'],
               'frank': ['explorer', 'boss_hunter', 'first_blood',
                         'explorer', 'first_blood', 'boss_hunter']}
    AchTrackerSystem.set_achs(players)
    print("")
    AchTrackerSystem.ach_analytics(players)
    print("")
    AchTrackerSystem.advanced_analytics(players)
    print("")
    AchTrackerSystem.ach_comparision('alice', 'bob', players)


if __name__ == "__main__":
    main()
