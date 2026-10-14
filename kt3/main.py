"""Пример запуска обработки каталога книг."""

from pathlib import Path
from books import get_books, filtered_books, books_total_cost


if __name__ == "__main__":
    filename = Path(__file__).with_name("books.csv")
    books = get_books(filename)
    query = input("Фрагмент названия книги: ")
    selected = filtered_books(books, query)
    print("Найденные книги:")
    print(*selected, sep="\n")
    print("Стоимость всего количества каждой найденной книги:")
    print(*books_total_cost(selected), sep="\n")
