"""Завдання 2: перевірка рядка на паліндром за допомогою deque."""

from collections import deque


def is_palindrome(text: str) -> bool:
    """Повертає True, якщо рядок є паліндромом (без урахування регістру та пробілів)."""
    chars = deque(ch.lower() for ch in text if not ch.isspace())

    # Порівнюємо символи з обох кінців; для непарної довжини
    # середній символ залишається в черзі й не потребує порівняння.
    while len(chars) > 1:
        if chars.popleft() != chars.pop():
            return False
    return True


if __name__ == "__main__":
    examples = [
        "А роза упала на лапу Азора",
        "Never odd or even",
        "abba",
        "racecar",
        "Hello world",
        "abca",
        "",
        "x",
    ]
    for example in examples:
        print(f"{example!r}: {'паліндром' if is_palindrome(example) else 'не паліндром'}")
