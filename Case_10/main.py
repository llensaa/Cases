import os
import sys
from typing import NoReturn
import utils
import navigation
import analysis
import search


def check_windows_environment() -> bool:
    """Проверка что программа запущена в Windows"""
    if not utils.is_windows_os():
        print('Программа предназначена только для Windows')
        sys.exit(1)
    return True


def display_windows_banner() -> None:
    """Отображение баннера с информацией о Windows"""
    drive = navigation.get_current_drive()
    print('=' * 60)
    print('ВИНДОУС ФАЙЛ МАНАГЕР')
    print(f'Текущий диск: {drive}')
    print(f'Рабочий каталог: {os.getcwd()}')
    print('=' * 60)


def display_main_menu(current_path: str) -> None:
    """Отображение главного меню для Windows"""
    print(f'\n Текущий путь: {current_path}\n')

    print('Навигация:')
    print('  cd <папка>   — перейти в подкаталог')
    print('  ..           — перейти в родительский каталог')
    print('  drive <буква>— сменить диск')

    print('\nИнструменты:')
    print('  analyze      — анализ текущего каталога')
    print('  search       — поиск файлов')
    print('  ls           — показать содержимое')

    print('\nСистема:')
    print('  drives       — доступные диски')
    print('  exit         — выход')


def handle_windows_navigation(command: str, current_path: str) -> str:
    """Обработка команд навигации в Windows"""
    parts = command.split(maxsplit=1)

    match parts[0]:
        case '..':
            new_path = navigation.move_up(current_path)
            return new_path or current_path

        case 'cd':
            if len(parts) < 2:
                print('Укажи имя папки')
                return current_path

            ok, new_path = navigation.move_down(current_path, parts[1])
            if not ok:
                print('Не удалось перейти в каталог')
                return current_path
            return new_path

        case 'drive':
            if len(parts) < 2:
                print('Укажи букву диска')
                return current_path

            drive = parts[1].upper() + ':\\'
            if drive[:-1] in navigation.list_available_drives():
                try:
                    os.chdir(drive)
                    return os.getcwd()
                except OSError:
                    print('Не удалось переключиться на диск')
                    return current_path
            else:
                print('Такого диска нет')
                return current_path

    return current_path


def handle_windows_analysis(command: str, current_path: str) -> None:
    """Обработка команд анализа Windows файловой системы"""
    if command == 'analyze':
        analysis.show_windows_directory_stats(current_path)


def handle_windows_search(command: str, current_path: str) -> None:
    """Обработка команд поиска в Windows"""
    if command == 'search':
        search.search_menu_handler(current_path)


def run_windows_command(command: str, current_path: str) -> str:
    """Главный обработчик команд"""
    match command.split()[0]:
        case 'cd' | '..' | 'drive':
            return handle_windows_navigation(command, current_path)

        case 'ls':
            ok, items = navigation.list_directory(current_path)
            if ok:
                navigation.format_directory_output(items)
            else:
                print('Ошибка доступа к каталогу')
            return current_path

        case 'analyze':
            handle_windows_analysis(command, current_path)
            return current_path

        case 'search':
            handle_windows_search(command, current_path)
            return current_path

        case 'drives':
            print('Доступные диски:')
            for d in navigation.list_available_drives():
                print(f'  {d}')
            return current_path

        case 'exit':
            print(' Выход')
            sys.exit(0)

        case _:
            print(' Неизвестная команда')
            return current_path


def main() -> NoReturn:
    """Главная функция программы для Windows"""
    check_windows_environment()
    display_windows_banner()

    current_path = os.getcwd()

    while True:
        try:
            display_main_menu(current_path)
            command = input('\n> ').strip()
            if not command:
                continue

            current_path = run_windows_command(command, current_path)

        except KeyboardInterrupt:
            print('\n Завершение работы')
            sys.exit(0)

        except Exception as e:
            print(f' Ошибка: {e}')


if __name__ == "__main__":
    main()
