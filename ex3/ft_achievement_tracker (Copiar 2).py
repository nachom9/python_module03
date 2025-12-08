#!/usr/bin/env python3


class AchievementTrackerSystem:


    unique_achievements = set()
    common_achievements = set()
    players = []

    def add_player(player):

        players = players + player

    def set_achievements(players: list) -> None:

        print("=== Achievement Tracker System ===\n")
        for player in players:
            print(f"Player {player.name} achievements:", player.achievements)

    def unique_achievement(players):

        print("=== Achievement Analytics ===")
        for player in players:
            if not unique_achievements:
                unique_achievements = player.achievements
            else:
                unique_achievements = unique_achievements.union(player.achievements)
        print("All unique achievements:", unique_achievements)
        print("Total unique achievements:", len(unique_achievements))
    
    def common_achievement(players):

        for player in players:
            if not common_achievements:
                common_achievements = player.achievements
            else:
                common_achievements = common_achievements.intersection(player.achievements)
        print("Common to all players:", common_achievements)

    #def rare_achievement(players):

        



class Player():

    def __init__(self, name, achievements):
        self.name = name
        self.achievements = achievements

if __name__ == "__main__":

    alice = Player("alice", {'first_kill', 'level_10', 
                                   'treasure_hunter', 'speed_demon'})
    bob = Player("bob", {'first_kill', 'level_10', 
                             'boss_slayer', 'collector'})
    charlie = Player("charlie", {'level_10', 'treasure_hunter',
                            'boss_slayer', 'speed_demon', 'perfectionist'})
    players = [alice, bob, charlie]
    AchievementTrackerSystem.set_achievements(players)
    print("")
    AchievementTrackerSystem.unique_achievement(players)
    print("")
    AchievementTrackerSystem.common_achievement(players)
