"""Функции для обработки файла books.csv без циклов в функциях обработки."""

import csv


def get_books(filename):
    """Читает CSV с разделителем | и преобразует типы quantity и price."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as file:
        rows = csv.DictReader(file, delimiter="|")
        return list(map(
            lambda row: [
                row["isbn"],
                row["title"],
                row["author"],
                int(row["quantity"]),
                float(row["price"]),
            ],
            rows,
        ))


def filtered_books(books, substring):
    """Оставляет книги, в названии которых есть substring (без учёта регистра)."""
    needle = substring.casefold()
    return list(map(
        lambda book: [book[0], f"{book[1]}, {book[2]}", book[3], book[4]],
        filter(lambda book: needle in book[1].casefold(), books),
    ))


def books_total_cost(filtered):
    """Возвращает пары (isbn, стоимость всего тиража)."""
    return list(map(lambda book: (book[0], book[2] * book[3]), filtered))
