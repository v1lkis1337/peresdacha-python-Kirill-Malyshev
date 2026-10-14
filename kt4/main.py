from user import User, SuperUser


if __name__ == "__main__":
    first = User("Анна", "anna", "pass1", 1)
    second = User("Борис", "boris", "pass2", 2)
    third = User("Вера", "vera", "pass3", 3)
    admin = SuperUser("Администратор", "admin", "secret", "администратор", 5)

    first.show_info()
    admin.show_info()
    print("Первый пользователь меньше второго:", first < second)
    print("Второй пользователь равен третьему:", second == third)
    print("Пользователей:", User.count)
    print("Суперпользователей:", SuperUser.count)
