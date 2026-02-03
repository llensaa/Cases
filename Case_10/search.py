import os
import re
from typing import List, Dict, Any
import utils
import navigation
import analysis


def find_files_windows(pattern: str, path: str, case_sensitive: bool = False) -> List[str]:
    """Поиск файлов по шаблону в Windows"""
    results = []

    regex = re.escape(pattern).replace(r'\*', '.*').replace(r'\?', '.')
    flags = 0 if case_sensitive else re.IGNORECASE
    compiled = re.compile(regex, flags)

    def walk(current: str, depth: int = 0):
        try:
            if depth > 20:
                return
            status, items = navigation.list_directory(current)
            if not status:
                return

            for item in items:
                full = os.path.join(current, item['name'])

                if item['type'] == 'file' and compiled.search(item['name']):
                    results.append(full)

                if item['type'] == 'directory' and not item['hidden'] \
                        and not analysis.is_system_file(item['name']):
                    walk(full, depth + 1)

        except (PermissionError, FileNotFoundError, OSError, RecursionError):
            return

    try:
        walk(path)
    except Exception:
        pass

    return results


def find_by_windows_extension(extensions: List[str], path: str) -> List[str]:
    """Поиск файлов по списку расширений Windows"""
    results = []
    exts = {e.lower() if e.startswith('.') else '.' + e.lower() for e in extensions}

    def walk(current: str, depth: int = 0):
        try:
            if depth > 20:
                return
            status, items = navigation.list_directory(current)
            if not status:
                return

            for item in items:
                full = os.path.join(current, item['name'])

                if item['type'] == 'file':
                    _, ext = os.path.splitext(item['name'])
                    if ext.lower() in exts:
                        results.append(full)

                if item['type'] == 'directory' and not item['hidden'] \
                        and not analysis.is_system_file(item['name']):
                    walk(full, depth + 1)

        except (PermissionError, FileNotFoundError, OSError, RecursionError):
            return

    try:
        walk(path)
    except Exception:
        pass

    return results


def find_large_files_windows(min_size_mb: float, path: str) -> List[Dict[str, Any]]:
    """Поиск крупных файлов в Windows"""
    results = []
    min_bytes = min_size_mb * 1024 * 1024

    def walk(current: str, depth: int = 0):
        try:
            if depth > 20:
                return
            status, items = navigation.list_directory(current)
            if not status:
                return

            for item in items:
                full = os.path.join(current, item['name'])

                if item['type'] == 'file' and item['size'] >= min_bytes:
                    _, ext = os.path.splitext(item['name'])
                    results.append({
                        'path': full,
                        'size_mb': item['size'] / (1024 * 1024),
                        'type': ext
                    })

                if item['type'] == 'directory' and not item['hidden'] \
                        and not analysis.is_system_file(item['name']):
                    walk(full, depth + 1)

        except (PermissionError, FileNotFoundError, OSError, RecursionError):
            return

    try:
        walk(path)
    except Exception:
        pass

    return sorted(results, key=lambda x: x['size_mb'], reverse=True)


def find_windows_system_files(path: str) -> List[str]:
    """Поиск системных файлов Windows"""
    results = []
    system_exts = {'.exe', '.dll', '.sys', '.msi'}
    system_dirs = {'windows', 'system32', 'program files'}

    special_folders = navigation.get_windows_special_folders().values()

    def walk(current: str, depth: int = 0):
        try:
            if depth > 10:
                return
            status, items = navigation.list_directory(current)
            if not status:
                return

            for item in items:
                full = os.path.join(current, item['name'])

                if item['type'] == 'file':
                    _, ext = os.path.splitext(item['name'])
                    if ext.lower() in system_exts:
                        low = full.lower()
                        if any(d in low for d in system_dirs):
                            results.append(full)

                if item['type'] == 'directory' and not any(
                        full.lower().startswith(s.lower()) for s in special_folders):
                    walk(full, depth + 1)

        except (PermissionError, FileNotFoundError, OSError, RecursionError):
            return

    try:
        walk(path)
    except Exception:
        pass

    return results


def search_menu_handler(current_path: str) -> bool:
    """Обработчик меню поиска для Windows"""
    print('\n1 — По шаблону\n2 — По расширению\n3 — Крупные файлы\n4 — Системные файлы\n5 — Статистика\n6 — Назад')
    choice = input('Выбор: ').strip()

    match choice:
        case '1':
            try:
                pattern = input('Шаблон: ')
                res = find_files_windows(pattern, current_path)
                format_windows_search_results(res, 'pattern')
            except Exception:
                print('Ошибка поиска')

        case '2':
            try:
                ext = input('Расширения: ').split(',')
                res = find_by_windows_extension(ext, current_path)
                format_windows_search_results(res, 'extension')
            except Exception:
                print('Ошибка поиска')

        case '3':
            try:
                size = float(input('Минимальный размер (MB): '))
                res = find_large_files_windows(size, current_path)
                format_windows_search_results(res, 'large')
            except ValueError:
                print('Некорректный размер')
            except Exception:
                print('Ошибка поиска')

        case '4':
            try:
                res = find_windows_system_files(current_path)
                format_windows_search_results(res, 'system')
            except Exception:
                print('Ошибка поиска')

        case '5':
            try:
                analysis.show_windows_directory_stats(current_path)
            except Exception:
                print('Ошибка получения статистики')

        case '6':
            return False

    return True


def format_windows_search_results(results: List, search_type: str) -> None:
    """Форматированный вывод результатов поиска для Windows"""
    if not results:
        print('Ничего не найдено')
        return

    try:
        if search_type in {'pattern', 'extension', 'system'}:
            for r in results[:20]:
                try:
                    size = utils.format_size(os.path.getsize(r))
                    print(f'{r} [{size}]')
                except Exception:
                    print(r)

        elif search_type == 'large':
            for r in results:
                print(f"{r['path']} — {r['size_mb']:.1f} MB")

    except Exception:
        print('Ошибка форматирования результатов')

    try:
        base = results[0] if isinstance(results[0], str) else results[0]['path']
        parent = os.path.dirname(base)
        if parent:
            stats = analysis.get_windows_file_attributes_stats(parent)
            print('\nАтрибуты:')
            for k, v in stats.items():
                print(f'    {k}: {v}')
    except Exception:
        pass
