#!/usr/bin/env python3


class AchievementTrackerSystem:

    alice_achievements = []
    bob_achievements = []
    charlie_achievements = []

    def set_achievements():

        print("=== Achievement Tracker System ===\n")

        alice_achievements = ['first_kill', 'level_10', 'treasure_hunter', 
                          'speed_demon']
        bob_achievements = ['first_kill', 'level_10', 'boss_slayer', 'collector']
        charlie_achievements = ['level_10', 'treasure_hunter', 
                            'boss_slayer', 'speed_demon', 'perfectionist']

        print("Player alice achievements:", alice_achievements)
        print("Player bob achievements:", bob_achievements)
        print("Player charlie achievements:", charlie_achievements)


    def achievement_analytics():

        unique_achievements = intersection()

class Player:

    def __init__(self, name, achievements):
        self.name = name
        self.achievements = achievements

if __name__ == "__main__":
    alice = alice.player("alice", [
    set_achievements()
    print("")
    achievement_analytics()
    
