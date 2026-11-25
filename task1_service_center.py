"""Завдання 1: імітація системи обробки заявок у сервісному центрі.

Використовується клас Queue з модуля queue.
"""

import random
from queue import Queue

# Створити чергу заявок
queue = Queue()

# Лічильник для унікальних номерів заявок
_request_counter = 0


def generate_request():
    """Створює нову заявку та додає її до черги."""
    global _request_counter
    _request_counter += 1
    request = {
        "id": _request_counter,
        "description": random.choice(
            ["Ремонт ноутбука", "Заміна екрана", "Чистка ПК", "Встановлення ПЗ", "Діагностика"]
        ),
    }
    queue.put(request)
    print(f"[+] Нова заявка #{request['id']}: {request['description']} (у черзі: {queue.qsize()})")


def process_request():
    """Видаляє заявку з черги та обробляє її, якщо черга не пуста."""
    if not queue.empty():
        request = queue.get()
        print(f"[✓] Оброблено заявку #{request['id']}: {request['description']} (у черзі: {queue.qsize()})")
    else:
        print("[!] Черга пуста, немає заявок для обробки")


def main():
    """Головний цикл програми: працює, поки користувач не вийде (Ctrl+C або 'q')."""
    print("Сервісний центр запущено. Enter — наступний крок, 'q' — вихід.")
    try:
        while True:
            # Виконати generate_request() для створення нових заявок
            for _ in range(random.randint(0, 3)):
                generate_request()
            # Виконати process_request() для обробки заявок
            process_request()

            command = input("> ").strip().lower()
            if command == "q":
                break
    except (KeyboardInterrupt, EOFError):
        pass
    print(f"Роботу завершено. Необроблених заявок у черзі: {queue.qsize()}")


if __name__ == "__main__":
    main()
