## https://www.youtube.com/watch?v=7fSHTqM8gHs

# Tip1 : raise NotImplementedError instead of "pass" or "..."
def connect():
    str = f'error : {connect.__name__} {connect}'
    raise NotImplementedError(str)
    # pass
    # ...


# connect()

# Tip2 : always specify return types
# Tip3 : use docstrings for extra info
def get_user() -> dict[int, str]:
    """
    Retrieves the ids and usernames from a database as a dict.

    :return: a dictionary of users
    """
    users: dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Top'}
    return users
    # return {1: 'Bob', 2: 'Jef', 3: 'Top'}


def display_users(users: dict[int, str]) -> None:
    """
    Prints each user to the console in a nice format.

    :param users: The users to display
    :return:
    """
    for k, v in users.items():
        print(k, v, sep=': ')


def main() -> None:
    users: dict[int, str] = get_user()
    display_users(users)


if __name__ == '__main__':
    main()

# Tip4 : force keyword args for complex functions with *,
from enum import Enum


class Quality(Enum):
    LOW: int = 400
    MEDIUM: int = 1000
    HIGH: int = 1440


class Privacy(Enum):
    PRIVATE: str = 'Private'
    UNLISTED: str = 'Unlisted'
    PUBLIC: str = 'Public'


def upload(file: str, *, quality: Quality, privacy: Privacy) -> None:
    print(f'Uploading: {file} in {quality.value}p ({privacy.value}')


def main() -> None:
    upload('cat.mp4',
           quality=Quality.LOW,
           privacy=Privacy.PRIVATE)


if __name__ == '__main__':
    main()


# Tip5 : use *args to collect variable arguments

def join_text(*strings, sep: str) -> str:
    return sep.join(strings)


def main() -> None:
    print(join_text('A', 'B', 'C', 'D', sep='-'))
    print(join_text('A', 'B', 'C', 'D', 'Z', sep='/'))


if __name__ == '__main__':
    main()
