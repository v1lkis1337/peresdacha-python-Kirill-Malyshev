"""Простая консольная ToDo с хранением задач в текстовом файле."""

from datetime import date, datetime
from pathlib import Path

TASKS_FILE = Path(__file__).with_name("tasks.txt")
RESET = "\033[0m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"


def load_tasks():
    if not TASKS_FILE.exists():
        return []
    tasks = []
    with TASKS_FILE.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip("\n")
            if "|" not in line:
                continue
            date_text, description = line.split("|", 1)
            try:
                due_date = date.fromisoformat(date_text)
            except ValueError:
                continue
            tasks.append((due_date, description))
    return tasks


def save_tasks(tasks):
    with TASKS_FILE.open("w", encoding="utf-8") as file:
        for due_date, description in tasks:
            file.write(f"{due_date.isoformat()}|{description}\n")


def task_color(due_date):
    today = date.today()
    if due_date < today:
        return RED, "Просрочено"
    if due_date == today:
        return YELLOW, "На сегодня"
    return GREEN, "Будущее"


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return
    for index, (due_date, description) in enumerate(tasks, start=1):
        color, status = task_color(due_date)
        print(f"{color}{index}. {due_date.isoformat()} — {description} [{status}]{RESET}")


def add_task(tasks):
    while True:
        date_text = input("Срок (ГГГГ-ММ-ДД): ").strip()
        try:
            due_date = datetime.strptime(date_text, "%Y-%m-%d").date()
            break
        except ValueError:
            print("Неверный формат даты.")
    description = input("Описание задачи: ").strip()
    if description:
        tasks.append((due_date, description))
        save_tasks(tasks)
        print("Задача сохранена.")


def main():
    tasks = load_tasks()
    while True:
        print("\n1 — показать задачи\n2 — добавить задачу\n0 — выход")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "0":
            break
        else:
            print("Неизвестная команда.")


if __name__ == "__main__":
    main()
