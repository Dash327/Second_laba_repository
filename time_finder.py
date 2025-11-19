import re
import requests
import sys
import os

# Регулярное выражение для времени ЧЧ:ММ:СС
TIME_PATTERN = r"\b(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d\b"
TIME_REGEX = re.compile(TIME_PATTERN)


def find_times_in_text(text: str):
    return TIME_REGEX.findall(text)


def main():
    print("Поиск времени в формате ЧЧ:ММ:СС")
    print("Выберите режим:")
    print("1. Пользовательский ввод")
    print("2. Поиск в локальном файле")

    try:
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            text = input("Введите текст: ")
            times = find_times_in_text(text)
            print(f"Найдено {len(times)} совпадений: {times}")

        elif choice == "2":
            filename = input("Введите путь к файлу: ").strip()
            if not os.path.exists(filename):
                print(f"Файл не найден: {filename}")
                return
            try:
                with open(filename, "r", encoding="utf-8") as f:
                    text = f.read()
                times = find_times_in_text(text)
                print(f"Найдено {len(times)} совпадений в файле.")
                if times:
                    print("Примеры:", times[:5])
            except Exception as e:
                print(f"Ошибка чтения файла: {e}")

        else:
            print("❗ Неверный выбор.")

    except KeyboardInterrupt:
        print("\nПрограмма завершена.")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()
