#!/usr/bin/env python3

class ListExamples:

    @staticmethod
    def show_high_scorers(players: list):

        high_scorers = [player for player in players if
                        players[player]['score'] > 2000]
        print(f"High scorers (>2000): {high_scorers}")

    @staticmethod
    def show_double_scores(players: list):

        double_scores = [players[player]['score'] * 2 for player in players]
        print(f"Scores doubled: {double_scores}")

    @staticmethod
    def show_active_players(players: list):

        active_players = [player for player in players if
                          players[player]['active']]
        print(f"Active players: {active_players}")

    @staticmethod
    def get_active_players(players: list):

        active_players = [player
                          for player in players if players[player]['active']]
        return active_players


class DictExamples:

    @staticmethod
    def show_scores(players: dict):

        scores = {}
        for player in players:
            scores[player] = players[player]['score']
        print(f"Player scores: {scores}")

    @staticmethod
    def show_categories(players: dict):

        categories = {
            "high": 0,
            "medium": 0,
            "low": 0,
            }

        for player in players:
            if players[player]['score'] >= 2000:
                categories['high'] += 1
            elif 2000 > players[player]['score'] >= 1800:
                categories['medium'] += 1
            elif players[player]['score'] < 1800:
                categories['low'] += 1

        print(f"Score categories: {categories}")

    @staticmethod
    def show_achievements(players: list):

        achievement_count = {}
        for player in players:
            achievement_count[player] = len(players[player]['achievements'])

        print(f"Achievement counts: {achievement_count}")


class SetExamples:

    def show_unique_players(players):

        unique_players = set(players)
        print(f"Unique players: {unique_players}")

    def show_unique_achievements(players):

        unique_achievements = {ach
                               for player in players
                               for ach in players[player]['achievements']}

        print(f"Unique achievements: {unique_achievements}")

    def show_active_regions(players):

        active_regions = {players[player]['region']
                          for player in players if players[player]['active']}
        print(f"Active regions: {active_regions}")


class CombinedAnalysis:

    def count_total_players(players):

        print(f"Total players: {len(players)}")

    def count_unique_achievements(players):

        unique_achievements = {ach
                               for player in players
                               for ach in players[player]['achievements']}

        print(f"Total unique achievements: {len(unique_achievements)}")

    def average_score(players):

        total_score = sum(players[player]['score'] for player in players)
        average_score = total_score / len(players)
        print(f"Average score: {average_score}")

    def top_performer(players):

        max_score = 0

        for player in players:
            if players[player]['score'] > max_score:
                max_score = players[player]['score']
                top_performer = player

        print(f"Top performer: {top_performer} "
              f"({players[top_performer]['score']} points, "
              f"{len(players[top_performer]['achievements'])} achievements)")


def main():

    print("=== Game Analytics Dashboard ===\n")
    players = {
        'alice': {
            "name": "Alice",
            "score": 2300,
            "achievements": {"treasure_hunter", "first_kill", "level_10",
                             "speed_demon", "perfectionist"},
            "region": "Spain",
            "active": True
        },
        'bob': {
            "name": "Bob",
            "score": 1800,
            "achievements": {"level_10", "collector", "boss_slayer"},
            "region": "Portugal",
            "active": True
        },
        'charlie': {
            "name": "Charlie",
            "score": 2150,
            "achievements": {"treasure_hunter", "boss_slayer",
                             "level_10", "speed_demon"},
            "region": "Germany",
            "active": True
        },
        'gaster': {
            "name": "Gaster",
            "score": 1500,
            "achievements": {"treasure_hunter", "boss_slayer",
                             "level_10", "speed_demon"},
            "region": "France",
            "active": True
        },
        'asgore': {
            "name": "Asgore",
            "score": 1750,
            "achievements": {"treasure_hunter", "boss_slayer",
                             "level_10", "speed_demon"},
            "region": "Norway",
            "active": False
        },
        'diana': {
            "name": "Diana",
            "score": 2050,
            "achievements": {"level_10", "collector", "boss_slayer",
                             "first_kill", "perfectionist", "speed_demon"},
            "region": "France",
            "active": False
        }
    }
    ListExamples.get_active_players(players)
    print("=== List Comprehension Examples ===")
    ListExamples.show_high_scorers(players)
    ListExamples.show_double_scores(players)
    ListExamples.show_active_players(players)
    print("\n=== Dict Comprehension Examples ===")
    DictExamples.show_scores(players)
    DictExamples.show_categories(players)
    DictExamples.show_achievements(players)
    print("\n=== Set Comprehension Examples ===")
    SetExamples.show_unique_players(players)
    SetExamples.show_unique_achievements(players)
    SetExamples.show_active_regions(players)
    print("\n=== Combined Analysis ===")
    CombinedAnalysis.count_total_players(players)
    CombinedAnalysis.count_unique_achievements(players)
    CombinedAnalysis.average_score(players)
    CombinedAnalysis.top_performer(players)


if __name__ == "__main__":
    main()
