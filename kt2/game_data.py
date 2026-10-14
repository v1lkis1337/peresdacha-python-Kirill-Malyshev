"""Данные и функции игры «Виселица»."""

import random
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
WORDS_FILE = BASE_DIR / "data" / "words.txt"
PARTS_DIR = BASE_DIR / "data" / "hangman_parts"


def load_words():
    """Возвращает список непустых слов из текстового файла."""
    with WORDS_FILE.open(encoding="utf-8") as file:
        return [line.strip().upper() for line in file if line.strip()]


def load_hangman_part(number):
    """Читает очередную часть рисунка из отдельного файла."""
    part_file = PARTS_DIR / f"{number}.txt"
    if not part_file.exists():
        return ""
    return part_file.read_text(encoding="utf-8")


def show_progress(word, guessed_letters):
    """Формирует строку с открытыми и скрытыми буквами."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def ask_letter(guessed_letters):
    """Запрашивает одну ещё не названную букву."""
    while True:
        letter = input("Введите одну букву: ").strip().upper()
        if len(letter) == 1 and letter.isalpha() and letter not in guessed_letters:
            return letter
        print("Введите одну новую букву.")


def play_round(word):
    """Проводит один раунд; возвращает True при победе."""
    guessed_letters = set()
    wrong_answers = 0
    max_errors = len(list(PARTS_DIR.glob("*.txt")))

    while wrong_answers < max_errors:
        print("\n" + show_progress(word, guessed_letters))
        letter = ask_letter(guessed_letters)
        guessed_letters.add(letter)

        if letter in word:
            print("Верно!")
            if all(symbol in guessed_letters for symbol in word):
                print(f"Победа! Загаданное слово: {word}")
                return True
        else:
            wrong_answers += 1
            print(load_hangman_part(wrong_answers))
            print("Такой буквы нет.")

    print(f"Вы проиграли. Было загадано слово: {word}")
    return False


def start_game():
    """Запускает игру и предлагает повторить раунд."""
    words = load_words()
    if not words:
        print("Файл со словами пуст. Добавьте слова в data/words.txt.")
        return

    while True:
        play_round(random.choice(words))
        answer = input("Сыграть ещё раз? (д/н): ").strip().lower()
        if answer not in ("д", "да", "y", "yes"):
            print("Спасибо за игру!")
            break
