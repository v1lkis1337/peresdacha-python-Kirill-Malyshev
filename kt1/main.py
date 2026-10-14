"""Интерактивная игра «Глухая бабушка»."""

import random


def main():
    print("Говори с бабушкой. Чтобы закончить разговор, крикни ПОКА! три раза подряд.")
    goodbye_count = 0

    while goodbye_count < 3:
        phrase = input("Внучек: ")

        if phrase == "ПОКА!":
            goodbye_count += 1
            if goodbye_count < 3:
                print("БАБУШКА: НЕ УХОДИ, ВНУЧЕК!")
            continue

        goodbye_count = 0
        if phrase.isupper():
            year = random.randint(1930, 1950)
            print(f"НЕТ, НИ РАЗУ С {year} ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")

    print("ДО СВИДАНИЯ, ВНУЧЕК!")


if __name__ == "__main__":
    main()
