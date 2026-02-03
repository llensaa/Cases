
import os
import sys
from typing import NoReturn
import utils
import navigation
import analysis
import search


def check_windows_environment() -> bool:
    """
    Verifies that the program is running on Windows OS.
    Exits the program if not running on Windows.
    
    Returns:
        bool: True if running on Windows (always returns True, exits otherwise).
    """
    if not utils.is_windows_os():
        print('Программа предназначена только для Windows')
        sys.exit(1)
    return True


def display_windows_banner() -> None:
    """
    Displays program banner with Windows-specific information.
    Shows current drive and working directory.
    
    Returns:
        None: Outputs information to console.
    """
    drive = navigation.get_current_drive()
    print('=' * 60)
    print('ВИНДОУС ФАЙЛ МАНАГЕР')
    print(f'Текущий диск: {drive}')
    print(f'Рабочий каталог: {os.getcwd()}')
    print('=' * 60)


def display_main_menu(current_path: str) -> None:
    """
    Displays the main menu interface for Windows file manager.
    Shows current path and available commands.
    
    Args:
        current_path (str): Current working directory path.
    
    Returns:
        None: Outputs menu to console.
    """
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
    """
    Handles navigation commands in Windows filesystem.
    Processes directory navigation and drive changes.
    
    Args:
        command (str): Navigation command (e.g., "cd folder", "..", "drive C").
        current_path (str): Current working directory path.
    
    Returns:
        str: New path after navigation, or same path if navigation failed.
    """
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
                    print('Укажи букву диска (например: drive D)')
                    return current_path

                drive_letter = parts[1].upper().strip(':')
                drive = f'{drive_letter}:\\'

                available_drives = navigation.list_available_drives()
                if drive not in available_drives:
                    print(f'Доступные диски: {", ".join(available_drives)}')
                    return current_path

                try:
                    os.chdir(drive)
                    return os.getcwd()
                except OSError:
                    print('Ошибка')
                    return current_path




def handle_windows_analysis(command: str, current_path: str) -> None:
    """
    Handles analysis commands for Windows filesystem.
    Processes directory analysis and statistics.
    
    Args:
        command (str): Analysis command.
        current_path (str): Current working directory path.
    
    Returns:
        None: Executes analysis and displays results.
    """
    if command == 'analyze':
        analysis.show_windows_directory_stats(current_path)


def handle_windows_search(command: str, current_path: str) -> None:
    """
    Handles search commands in Windows filesystem.
    Processes file search operations.
    
    Args:
        command (str): Search command.
        current_path (str): Current working directory path.
    
    Returns:
        None: Executes search and displays results.
    """
    if command == 'search':
        search.search_menu_handler(current_path)


def run_windows_command(command: str, current_path: str) -> str:
    """
    Main command handler for Windows file manager.
    Routes commands to appropriate handlers.
    
    Args:
        command (str): User command input.
        current_path (str): Current working directory path.
    
    Returns:
        str: Updated current path after command execution.
    """
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
    """
    Main function for Windows file manager program.
    Initializes and runs the command-line interface.
    
    Returns:
        NoReturn: Program runs indefinitely until exit command.
    """
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
