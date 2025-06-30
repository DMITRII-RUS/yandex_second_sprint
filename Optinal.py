from typing import Optional


class User:
    def __init__(
            self,
            first_name: Optional[str] = None,
            last_name: Optional[str] = None,
            username: Optional[str] = None,
    ):
        if not first_name and not last_name and not username:
            raise ValueError('Необходимо указать параметры пользователя')

        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    # Опишите метод класса with_name.
    @classmethod
    def with_name(
        cls, first_name: Optional[str], last_name: Optional[str]
    ):
        if not (first_name and first_name.strip() and last_name and last_name.strip()):
            raise ValueError
        return cls(first_name=first_name, last_name=last_name, username=None)
    # Опишите метод класса with_username.

    @classmethod
    def with_username(
        cls, username: Optional[str]
    ):
        if not User.is_username_allowed(username):
            raise ValueError('Некорректное имя пользователя')
        return cls(first_name=None, last_name=None, username=username)

    # Опишите статический метод класса is_username_allowed.
    @staticmethod
    def is_username_allowed(username: Optional[str]):
        try:
            if username is None:
                return False
            elif username.lower().startswith('admin'):
                return False
            else:
                return True
        except ValueError:
            return False

    # Опишите метод-свойство full_name.
    @property
    def full_name(self) -> str:
        if (self.first_name is not None and self.last_name is not None and
                self.first_name.strip() and self.last_name.strip()):
            return f"{self.first_name} {self.last_name}"
        if self.username is not None and self.username.strip():
            return f'@{self.username}'
        return ''


stas = User.with_name('Стас', 'Басов')
print(stas.full_name)

# Попробуем создать пользователя с "запрещённым" именем.
# ne_stas = User.with_username('admin_nestas_anonymous')
