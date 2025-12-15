#!/usr/bin/env python3

class ListExamples:

    @staticmethod
    def show_high_scorers(players: list):

        high_scorers = [player['name'] for player in players if
                        player['score'] > 2000]
        print(f"High scorers (>2000): {high_scorers}")

    @staticmethod
    def show_double_scores(players: list):

        double_scores = [player['score'] * 2 for player in players]
        print(f"Scores doubled: {double_scores}")

    @staticmethod
    def show_active_players(players: list):

        active_players = [player['name'] for player in players if
                          player['active']]
        print(f"Active players: {active_players}")

    @staticmethod
    def get_active_players(players: list):

        active_players = [player for player in players if player['active']]
        return active_players


class DictExamples:

    @staticmethod
    def show_scores(active_players: list):

        scores = {}
        for player in active_players:
            scores[player['name']] = player['score']
        print(scores)

    @staticmethod
    def show_categories(players: list):

        categories = {
            "high": 0,
            "medium": 0,
            "low": 0,
            }

        for player in players:
            if player['score'] >= 2000:
                categories['high'] += 1
            elif 2000 > player['score'] >= 1800:
                categories['medium'] += 1
            elif player['score'] < 1800:
                categories['low'] += 1

        print(f"Score categories: {categories}")

    @staticmethod
    def show_achievements(players: list):

        achievement_count = {}
        for player in players:
            achievement_count[player['name']] = len(player['achievements'])

        print(f"Achievement counts: {achievement_count}")


def main():

    print("=== Game Analytics Dashboard ===\n")
    alice = {
        "name": "Alice",
        "score": 2300,
        "achievements": {"treasure_hunter", "first_kill", "level_10",
                         "speed_demon", "perfectionist"},
        "active": True
    }
    bob = {
        "name": "Bob",
        "score": 1800,
        "achievements": {"level_10", "collector", "boss_slayer"},
        "active": True
    }
    charlie = {
        "name": "Charlie",
        "score": 2150,
        "achievements": {"treasure_hunter", "boss_slayer",
                         "level_10", "speed_demon"},
        "active": True
    }
    gaster = {
        "name": "Gaster",
        "score": 1500,
        "achievements": {"treasure_hunter", "boss_slayer",
                         "level_10", "speed_demon"},
        "active": True
    }
    asgore = {
        "name": "Asgore",
        "score": 1750,
        "achievements": {"treasure_hunter", "boss_slayer",
                         "level_10", "speed_demon"},
        "active": False
    }
    diana = {
        "name": "Diana",
        "score": 2050,
        "achievements": {"level_10", "collector", "boss_slayer",
                         "first_kill", "perfeccionist", "speed_demon"},
        "active": False
    }
    players = [alice, bob, charlie, diana, gaster, asgore]
    active_players = ListExamples.get_active_players(players)
    print("=== List Comprehension Examples ===")
    ListExamples.show_high_scorers(players)
    ListExamples.show_double_scores(players)
    ListExamples.show_active_players(players)
    print("")
    print("=== Dict Comprehension Examples ===")
    DictExamples.show_scores(active_players)
    DictExamples.show_categories(players)
    DictExamples.show_achievements(players)


if __name__ == "__main__":
    main()
