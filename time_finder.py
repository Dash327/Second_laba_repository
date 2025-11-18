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
    print("2. Поиск на веб-странице (по URL)")
    print("3. Поиск в локальном файле")

    try:
        choice = input("Ваш выбор: ").strip()
        
        if choice == "1":
            text = input("Введите текст: ")
            times = find_times_in_text(text)
            print(f"Найдено {len(times)} совпадений: {times}")
