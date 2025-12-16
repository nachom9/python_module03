#!/usr/bin/env python3

import sys


def show_scores(scores: list) -> None:

    print("Scores processed: [", end="")
    print(*scores, sep=", ", end="")
    print("]")


def score_cruncher():

    scores = []
    argv_count = 1
    player_count = 0
    print("=== Player Score Analytics ===")
    while argv_count < len(sys.argv):
        try:
            scores.append(int(sys.argv[argv_count]))
            player_count += 1
        except ValueError:
            print(f"You must give numbers: '{sys.argv[argv_count]}' "
                  "is not a number")
        finally:
            argv_count += 1

    if not player_count:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    else:
        total_score = sum(scores)
        average_score = (total_score / player_count)
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        show_scores(scores)
        print("Total players:", player_count)
        print("Total scores:", total_score)
        print("Average score:", average_score)
        print("High score:", high_score)
        print("Low score:", low_score)
        print("Score range:", score_range)


if __name__ == "__main__":
    score_cruncher()
