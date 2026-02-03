import os
from typing import Dict, Any, List, Tuple
from collections import defaultdict
import utils  # Функции архитектора
import navigation  # Функции инженера навигации

SYSTEM_PATTERNS = { '$RECYCLE.BIN', 'System Volume Information',
    'pagefile.sys', 'hiberfil.sys', 'swapfile.sys'
}

def is_system_file(name: str) -> bool:
    return name in SYSTEM_PATTERNS or name.startswith('.')


def count_files(path: str) -> Tuple[bool, int]:
    """Рекурсивный подсчет файлов в Windows каталоге"""
    # TODO: Использовать navigation.list_directory() для получения содержимого
    # Рекурсивно обходить подкаталоги, игнорируя системные файлы Windows
    # Учитывать ограничения доступа через utils.safe_windows_listdir()
    # Вернуть (True, количество) при успехе, (False, 0) при ошибке
    def recurse_count(path: str) -> int:
        status, items = navigation.list_directory(path)
        if not status:
            return 0

        total = 0
        for item in items:
            if not item['hidden'] and not is_system_file(item['name']):
                match item['type']:
                    case 'file':
                        total += 1
                    case 'directory':
                        new_path = os.path.join(path, item['name'])
                        total += recurse_count(new_path)

        return total
    try:
        count = recurse_count(path)
        return True, count

    except (PermissionError, FileNotFoundError, OSError):
        return False, 0


def count_bytes(path: str) -> Tuple[bool, int]:
    """Рекурсивный подсчет размера файлов в Windows"""
    # TODO: Используя count_files() как основу, суммировать размеры файлов
    # Учесть что некоторые файлы могут быть недоступны для чтения размера
    # Пропускать junction points и symlinks чтобы избежать циклов
    def recurse_size(path: str) -> int:
        status, items = navigation.list_directory(path)
        if not status:
            return 0

        total = 0
        for item in items:
            if not item['hidden']:
                match item['type']:
                    case 'file':
                        total += item['size']
                    case 'directory':
                        new_path = os.path.join(path, item['name'])
                        total += recurse_size(new_path)
        return total

    try:
        size = recurse_size(path)
        return True, size

    except (PermissionError, FileNotFoundError, OSError):
        return False, 0


def analyze_windows_file_types(path: str) -> Tuple[bool, Dict[str, Dict[str, Any]]]:
    """Анализ типов файлов с учетом Windows расширений"""
    # TODO: Собрать статистику по расширениям характерным для Windows
    # .exe, .dll, .msi, .bat, .ps1, .docx, .xlsx и т.д.
    # Использовать navigation.list_directory() для получения файлов
    # Группировать по расширениям, считать количество и суммарный размер
    status, items = navigation.list_directory(path)
    if not status:
        return False, {}

    stats = defaultdict(lambda: {'count': 0, 'size': 0})

    for item in items:
        new_path = os.path.join(path, item['name'])
        if os.path.islink(new_path):
            continue

        if not item['hidden'] and not utils.is_hidden_windows_file(item['name']):
            extension = os.path.splitext(item['name'][1]) or 'no extension'
            extension.lower()
            match item['type']:
                case 'file':
                    stats[extension]['count'] += 1
                    stats[extension]['size'] += item.get('size')
                case 'directory':
                    new_path = os.path.join(path, item['name'])
                    check, rest = analyze_windows_file_types(new_path)
                    if check:
                        for extension, data in rest.items():
                            stats[extension]['count'] += data['count']
                            stats[extension]['size'] += data['size']

    return True, dict(stats)




def get_windows_file_attributes_stats(path: str) -> Dict[str, int]:
    """Статистика по атрибутам файлов Windows"""
    # TODO: Анализировать атрибуты: скрытые, системные, только для чтения
    # Использовать utils.is_hidden_windows_file() и другие проверки
    # Вернуть статистику: {'hidden': 5, 'system': 2, 'readonly': 10}
    status, items = navigation.list_directory(path)
    if not status:
        return {'hidden': 0, 'system': 0, 'readonly': 0}

    stats = {'hidden': 0, 'system': 0, 'readonly': 0}

    for item in items:
        new_path = os.path.join(path, item['name'])
        if os.path.islink(new_path):
            continue

        match item['type']:
            case 'file':
                if item['hidden']:
                    stats['hidden'] += 1
                elif utils.is_system_windows_file(new_path):
                    stats['system'] += 1
                elif utils.is_readonly_windows_file(new_path):
                    stats['readonly'] += 1
            case 'directory':
                new_stats = get_windows_file_attributes_stats(new_path)
                stats['hidden'] += new_stats['hidden']
                stats['system'] += new_stats['system']
                stats['readonly'] += new_stats['readonly']

    return stats


def show_windows_directory_stats(path: str) -> bool:
    """Комплексный вывод статистики Windows каталога"""
    # TODO: Использовать ВСЕ вышеперечисленные функции анализа
    # Вывести сводную информацию о каталоге:
    # - Общее количество файлов и папок
    # - Распределение по типам файлов
    # - Статистика по атрибутам
    # - Крупнейшие файлы
    # Вернуть True при успешном выполнении
    print('\n=====АНАЛИЗ КАТАЛОГА WINDOWS=====')
    print(f'Путь: {path}')

    file_status, file_count = count_files(path)
    if not file_status:
        print('Ошибка')
        return False

    print(f'\nВсего файлов: {file_count}')

    size_status, size_count = count_bytes(path)
    if size_status:
        print(f'Размер всех файлов: {utils.format_size(size_count)}')

    type_status, type_count = analyze_windows_file_types(path)
    if type_status:
        print('\nВстречающиеся типы файлов:')
        for extension, info in sorted(types.items(), key=lambda x: -x[1]['count']):
            print(f'    {extension}: {info['count']} файлов, {utils.format_size(info['size'])}')

    file_attrs = get_windows_file_attributes_stats(path)
    print('\nАтрибуты файлов:')
    for attr in file_attrs.keys():
        print(f'    {attr}: {file_attrs[attr]}')
