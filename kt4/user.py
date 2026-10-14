"""Классы User и SuperUser."""


class User:
    count = 0

    def __init__(self, name, login, password, grade):
        if not isinstance(grade, int) or isinstance(grade, bool) or grade <= 0:
            raise ValueError("grade должен быть положительным целым числом")
        self._name = name
        self._login = login
        self._password = password
        self._grade = grade
        User.count += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        print("Невозможно изменить логин!")

    @property
    def password(self):
        return "********"

    @password.setter
    def password(self, value):
        self._password = value

    @property
    def grade(self):
        raise AttributeError("Неизвестное свойство grade")

    @grade.setter
    def grade(self, value):
        raise AttributeError("Неизвестное свойство grade")

    def show_info(self):
        print(f"Имя: {self.name}; логин: {self.login}; пароль: {self.password}")

    def showInfo(self):
        self.show_info()

    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade == other._grade

    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade < other._grade

    def __gt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade > other._grade

    def eq(self, other):
        return self == other

    def lt(self, other):
        return self < other

    def gt(self, other):
        return self > other


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role, grade):
        super().__init__(name, login, password, grade)
        self._role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, value):
        self._role = value

    def show_info(self):
        print(f"Имя: {self.name}; логин: {self.login}; роль: {self.role}")
