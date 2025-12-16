#!/usr/bin/env python3

def get_data():

    return {
        'players': {
            'alice': {
                'level': 41,
                'total_score': 2824,
                'sessions_played': 13,
                'favorite_mode': 'ranked',
                'achievements_count': 5
            },
            'bob': {
                'level': 16,
                'total_score': 4657,
                'sessions_played': 27,
                'favorite_mode': 'ranked',
                'achievements_count': 2
            },
            'charlie': {
                'level': 44,
                'total_score': 9935,
                'sessions_played': 21,
                'favorite_mode': 'ranked',
                'achievements_count': 7
            },
            'diana': {
                'level': 3,
                'total_score': 1488,
                'sessions_played': 21,
                'favorite_mode': 'casual',
                'achievements_count': 4
            },
            'eve': {
                'level': 33,
                'total_score': 1434,
                'sessions_played': 81,
                'favorite_mode': 'casual',
                'achievements_count': 7
            },
            'frank': {
                'level': 15,
                'total_score': 8359,
                'sessions_played': 85,
                'favorite_mode': 'competitive',
                'achievements_count': 1
            }
        },
        'sessions': [
            {'player': 'bob', 'duration_minutes': 94,
             'score': 1831, 'mode': 'competitive', 'completed': False},
            {'player': 'bob', 'duration_minutes': 32,
             'score': 1478, 'mode': 'casual', 'completed': True},
            {'player': 'diana', 'duration_minutes': 17,
             'score': 1570, 'mode': 'competitive', 'completed': False},
            {'player': 'alice', 'duration_minutes': 98,
             'score': 1981, 'mode': 'ranked', 'completed': True},
        ],
        'game_modes': ['casual', 'competitive', 'ranked'],
        'achievements': [
            'first_blood', 'level_master', 'speed_runner',
            'treasure_seeker', 'boss_hunter', 'pixel_perfect',
            'combo_king', 'explorer'
        ]
    }


class ListExamples:

    @staticmethod
    def show_high_scorers(players: dict):

        high_scorers = [player for player in players if
                        players[player]['total_score'] > 2000]
        print(f"High scorers (>2000): {high_scorers}")

    @staticmethod
    def show_double_scores(players: dict):

        double_scores = [players[player]['total_score'] * 2
                         for player in players]
        print(f"Scores doubled: {double_scores}")

    @staticmethod
    def show_active_players(players: dict):

        active_players = [player for player in players]
        print(f"Active players: {active_players}")


class DictExamples:

    @staticmethod
    def show_scores(players: dict):

        scores = {player: players[player]['total_score']
                  for player in players}
        print(f"Player scores: {scores}")

    @staticmethod
    def show_categories(players: dict):

        categories = {
            "high": 0,
            "medium": 0,
            "low": 0,
            }

        for player in players:
            if players[player]['total_score'] >= 2000:
                categories['high'] += 1
            elif 2000 > players[player]['total_score'] >= 1800:
                categories['medium'] += 1
            elif players[player]['total_score'] < 1800:
                categories['low'] += 1

        print(f"Score categories: {categories}")

    @staticmethod
    def show_achievements(players: dict):

        achievement_count = {player: players[player]['achievements_count']
                             for player in players}
        print(f"Achievement counts: {achievement_count}")


class SetExamples:

    def show_unique_players(players):

        unique_players = set(player for player in players)
        print(f"Unique players: {unique_players}")

    def show_unique_achievements(data):

        unique_achievements = {ach
                               for ach in data['achievements']}

        print(f"Unique achievements: {unique_achievements}")

    def show_gamemodes(data):

        unique_gamemodes = {gamemode
                            for gamemode in data['game_modes']}
        print(f"Unique gamemodes: {unique_gamemodes}")


class CombinedAnalysis:

    def count_total_players(players):

        print(f"Total players: {len(players)}")

    def count_unique_achievements(data):

        print(f"Total unique achievements: {len(data['achievements'])}")

    def average_score(players):

        total_score = sum(players[player]['total_score'] for player in players)
        average_score = total_score / len(players)
        print(f"Average score: {average_score}")

    def top_performer(players):

        max_score = 0

        for player in players:
            if players[player]['total_score'] > max_score:
                max_score = players[player]['total_score']
                top_performer = player

        print(f"Top performer: {top_performer} "
              f"({players[top_performer]['total_score']} points, "
              f"{players[top_performer]['achievements_count']} achievements)")


def main():

    print("=== Game Analytics Dashboard ===\n")
    data = get_data()
    print("=== List Comprehension Examples ===")
    players = data['players']
    ListExamples.show_high_scorers(players)
    ListExamples.show_double_scores(players)
    ListExamples.show_active_players(players)
    print("\n=== Dict Comprehension Examples ===")
    DictExamples.show_scores(players)
    DictExamples.show_categories(players)
    DictExamples.show_achievements(players)
    print("\n=== Set Comprehension Examples ===")
    SetExamples.show_unique_players(players)
    SetExamples.show_unique_achievements(data)
    SetExamples.show_gamemodes(data)
    print("\n=== Combined Analysis ===")
    CombinedAnalysis.count_total_players(players)
    CombinedAnalysis.count_unique_achievements(data)
    CombinedAnalysis.average_score(players)
    CombinedAnalysis.top_performer(players)


if __name__ == "__main__":
    main()
