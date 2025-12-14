#!/usr/bin/env python3

class PlayerEvents:

    def __init__(self, name, level, gold):
        self.name = name
        self.level = level
        self.gold = gold

    def kill(self):
        event = (f"Event 1: Player {self.name} (level {self.level}) killed"
        f" a monster")
        return event

    def treasure(self):
        event = (f"Event 2: Player {self.name} (level {self.level}) found"
        f" treasure")
        self.gold += 25
        return event

    def level_up(self):
        event = (f"Event 3: Player {self.name} (level {self.level}) leveled"
        f" up")
        self.level += 1
        return event


class GameData:

    level_up_count = 0
    treasure_count = 0
    level10_count = 0
    event_count = 0

    @classmethod
    def event_creator(cls, players):

        j = 0
        for i in range(0, 1000):
            pj = players[j]
            if i % 7 == 0:
                event = pj.level_up()
                cls.level_up_count += 1
            elif i % 11 == 0:
                event = pj.treasure()
                cls.treasure_count += 1
            else:
                event = pj.kill()
            if j == 0:
                j = 1
            elif j == 1:
                j = 2
            elif j == 2:
                j = 0
            if pj.level >= 10:
                cls.level10_count += 1
            cls.event_count += 1
            yield event


    @classmethod
    def event_generator(cls, players):

        print("=== Game Data Stream Processor ===\n")
        print("Processing 1000 game events...\n")
        processed = cls.event_creator(players)

        for event in processed:
            print (event)

    @classmethod
    def stream_analytics(cls):

        print("=== Stream Analytics ===")
        print(f"Total events processed: {cls.event_count}")
        print(f"High-level players (10+): {cls.level10_count}")
        print(f"Treasure events: {cls.treasure_count}")
        print(f"Level-up events: {cls.level_up_count}")

def main():

    alice = PlayerEvents("Alice", 5, 0)
    bob = PlayerEvents("Bob", 12, 0)
    charlie = PlayerEvents("Charlie", 8, 0)
    players = [alice, bob, charlie]
    GameData.event_generator(players)
    print("")
    GameData.stream_analytics()

if __name__ == "__main__":
    main()
