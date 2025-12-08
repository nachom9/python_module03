#!/usr/bin/env python3


class AchievementTrackerSystem:


    unique_achievements = set()
    common_achievements = set()
    rare_achievements = set()
    all_players = set()


    def __init__(self, name, achievements):
        self.name = name
        self.achievements = achievements

    @staticmethod
    def add_player(self):

        AchievementTrackerSystem.all_players.add(self)

    @classmethod
    def set_achievements(cls) -> None:

        print("=== Achievement Tracker System ===\n")
        for player in cls.all_players:
            print(f"Player {player.name} achievements:", player.achievements)

    @classmethod
    def unique_achievement(cls):

        print("=== Achievement Analytics ===")
        for player in cls.all_players:
            if not cls.unique_achievements:
                cls.unique_achievements = player.achievements
            else:
                cls.unique_achievements = cls.unique_achievements.union(player.achievements)
        print("All unique achievements:", cls.unique_achievements)
        print("Total unique achievements:", len(cls.unique_achievements))
    
    @classmethod
    def common_achievement(cls):

        for player in cls.all_players:
            if not cls.common_achievements:
                cls.common_achievements = player.achievements
            else:
                cls.common_achievements = cls.common_achievements.intersection(player.achievements)
        print("Common to all players:", cls.common_achievements)

    @classmethod
    def rare_achievement(cls):
        for achievement in cls.unique_achievements:
            count = 0
            for player in cls.all_players:
                for ach in player.achievements:
                    if ach == achievement:
                        count += 1
            if count == 1:
                cls.rare_achievements.add(achievement)
        print("Rare achievements (1 player):", cls.rare_achievements)

        

if __name__ == "__main__":

    alice = AchievementTrackerSystem("alice", {'first_kill', 'level_10', 
                                   'treasure_hunter', 'speed_demon'})
    bob = AchievementTrackerSystem("bob", {'first_kill', 'level_10', 
                             'boss_slayer', 'collector'})
    charlie = AchievementTrackerSystem("charlie", {'level_10', 'treasure_hunter',
                            'boss_slayer', 'speed_demon', 'perfectionist'})
    AchievementTrackerSystem.add_player(alice)
    AchievementTrackerSystem.add_player(bob)
    AchievementTrackerSystem.add_player(charlie)
    AchievementTrackerSystem.set_achievements()
    print("")
    AchievementTrackerSystem.unique_achievement()
    print("")
    AchievementTrackerSystem.common_achievement()
    print("")
    AchievementTrackerSystem.rare_achievement()
