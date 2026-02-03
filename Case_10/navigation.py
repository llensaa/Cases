import os
from datetime import datetime
from typing import List, Dict, Any, Tuple
import utils
from utils import safe_windows_listdir


def get_current_drive() -> str:
    """Получение текущего диска Windows"""
    # TODO: Вернуть текущий диск (например: "C:")
    # Использовать os.path.splitdrive()
    drive, rest = os.path.splitdrive(os.getcwd())
    return drive


def list_available_drives() -> List[str]:
    """Получение списка доступных дисков Windows"""
    # TODO: Вернуть список доступных дисков (['C:', 'D:', ...])
    # Использовать os.listdir('/') не подойдет для Windows!
    # Исследовать: использовать win32api или другие методы
    drives = os.listdrives()
    return drives


def list_directory(path: str) -> Tuple[bool, List[Dict[str, Any]]]:
    """Отображение содержимого каталога в Windows"""
    # TODO: Используя utils.safe_windows_listdir(), получить содержимое
    # Для каждого элемента вернуть словарь с информацией:
    # {'name': 'file.txt', 'type': 'file', 'size': 1024, 'modified': '2024-01-15', 'hidden': False}
    # Использовать utils.is_hidden_windows_file() для проверки скрытых файлов
    # Вернуть (True, данные) при успехе, (False, []) при ошибке
    try:
        items = utils.safe_windows_listdir(path)
        results = []

        for name in items:
            full_path = os.path.join(path, name)
            stat = os.stat(name)
            item_type = 'directory' if os.path.isdir(full_path) else 'file'
            size = stat.st_size
            mod_time = stat.st_mtime
            modified = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            hidden = utils.is_hidden_windows_file(full_path)

            item_info = {'name': name,
                         'type': item_type,
                         'size': size,
                         'modified': modified,
                         'hidden': hidden}
            results.append(item_info)

        return True, results

    except (PermissionError, FileNotFoundError, OSError):
        return False, []


def format_directory_output(items: List[Dict[str, Any]]) -> None:
    """Форматированный вывод содержимого каталога для Windows"""
    # TODO: Красиво отформатировать вывод используя данные из list_directory()
    # Учесть что в Windows есть системные и скрытые файлы
    # Показать диски если находимся в корне
    if not items:
        print('Директория пуста или недоступна')
        return None

    files = [item for item in items if item['type'] == 'file']
    directories = [item for item in items if item['type'] == 'directory']

    files.sort(key=lambda x: x['name'].lower())
    directories.sort(key=lambda x: x['name'].lower())

    print('📁Директории:')
    for directory in directories:
        mark = '🔒' if directory['hidden'] else '📁'
        print(f'    {mark} {directory['name']}')

    print('\n📄 Файлы:')
    for file in files:
        mark = '🔒' if file['hidden'] else '📄'
        size = utils.format_size(file['size'])
        hidden_str = '[СКРЫТЫЙ]' if file['hidden'] else ''

        print(f'    {mark} {file['name']} {size} {hidden_str}')

    total_dirs = len(directories)
    total_files = len(files)
    total_hidden = sum(1 for item in items if item['hidden'])

    print(f'\n Всего: {total_dirs} папок, '
          f'{total_files} файлов, '
          f'{total_hidden} скрыто')


def move_up(current_path: str) -> str:
    """Переход в родительский каталог в Windows"""
    # TODO: Использовать utils.get_parent_path() для получения родителя
    # Проверить валидность нового пути через utils.validate_windows_path()
    # Учесть переход между дисками
    try:
        parent_path = utils.get_parent_path(current_path)
        if utils.validate_windows_path(parent_path):
            return parent_path
    except (OSError, PermissionError):
        return ''


def move_down(current_path: str, target_dir: str) -> Tuple[bool, str]:
    """Переход в указанный подкаталог в Windows"""
    # TODO: Проверить что target_dir существует через utils.safe_windows_listdir()
    # Сформировать новый путь и проверить через utils.validate_windows_path()
    # Вернуть (True, новый_путь) при успехе, (False, текущий_путь) при ошибке
    try:
        if target_dir in utils.safe_windows_listdir(current_path):
            new_path = os.path.normpath(os.path.join(current_path, target_dir))

            if utils.validate_windows_path(new_path):
                return True, new_path

    except (PermissionError, OSError):
        return False, current_path


def get_windows_special_folders() -> Dict[str, str]:
    """Получение путей к специальным папкам Windows"""
    # TODO: Вернуть словарь с путями к папкам:
    # {'Desktop': 'C:\\Users\\...', 'Documents': '...', 'Downloads': '...'}
    # Использовать os.environ для получения USERPROFILE и других переменных
    userprofile = os.environ.get('USERPROFILE')
    if not userprofile:
        return {}

    special_folders = {
        'Desktop': os.path.join(userprofile, 'Desktop'),
        'Documents': os.path.join(userprofile, 'Documents'),
        'Downloads': os.path.join(userprofile, 'Downloads')
    }
    return special_folders
