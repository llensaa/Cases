import os
import re
from typing import List, Dict, Any
import utils
import navigation
import analysis
import ru_local as ru


def find_files_windows(pattern: str, path: str, case_sensitive: bool = False) -> List[str]:
    """
    Searches for files matching a pattern in Windows directory tree.
    Supports wildcards (* and ?) in the pattern.

    Args:
        pattern (str): Search pattern with wildcards (e.g., "*.txt", "file?.doc").
        path (str): Root directory path to start searching from.
        case_sensitive (bool, optional): Whether search is case-sensitive. Defaults to False.

    Returns:
        List[str]: List of full paths to matching files.
    """
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
    """
    Searches for files with specified extensions in Windows directory tree.

    Args:
        extensions (List[str]): List of file extensions (e.g., ["txt", "docx", ".pdf"]).
        path (str): Root directory path to start searching from.

    Returns:
        List[str]: List of full paths to files with matching extensions.
    """
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
    """
    Finds large files exceeding specified minimum size in Windows directory tree.

    Args:
        min_size_mb (float): Minimum file size in megabytes.
        path (str): Root directory path to start searching from.

    Returns:
        List[Dict[str, Any]]: List of dictionaries with keys:
            'path' (str): Full file path,
            'size_mb' (float): File size in megabytes,
            'type' (str): File extension.
        Sorted by size in descending order.
    """
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
    """
    Finds Windows system files in specified directory.
    Identifies system files by location and extension patterns.

    Args:
        path (str): Root directory path to start searching from.

    Returns:
        List[str]: List of full paths to system files.
    """
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
    """
    Handles the search menu interface for Windows file operations.
    Displays search options and processes user choices.

    Args:
        current_path (str): Current working directory path.

    Returns:
        bool: True to continue showing menu, False to exit.
    """
    print(f'\n{ru.SEARCH_MENU_OPTIONS}')
    choice = input(f'{ru.CHOICE_PROMPT}: ').strip()

    match choice:
        case '1':
            try:
                pattern = input(f'{ru.PATTERN_PROMPT}: ')
                res = find_files_windows(pattern, current_path)
                format_windows_search_results(res, 'pattern')
            except Exception:
                print(f'{ru.SEARCH_ERROR}')

        case '2':
            try:
                ext = input(f'{ru.EXTENSIONS_PROMPT}: ').split(',')
                res = find_by_windows_extension(ext, current_path)
                format_windows_search_results(res, 'extension')
            except Exception:
                print(f'{ru.SEARCH_ERROR}')

        case '3':
            try:
                size = float(input(f'{ru.MIN_SIZE_PROMPT}'))
                res = find_large_files_windows(size, current_path)
                format_windows_search_results(res, 'large')
            except ValueError:
                print(f'{ru.INVALID_SIZE_ERROR}')
            except Exception:
                print(f'{ru.SEARCH_ERROR}')

        case '4':
            try:
                res = find_windows_system_files(current_path)
                format_windows_search_results(res, 'system')
            except Exception:
                print(f'{ru.SEARCH_ERROR}')

        case '5':
            try:
                analysis.show_windows_directory_stats(current_path)
            except Exception:
                print(f'{ru.STATS_ERROR}')

        case '6':
            return False

    return True


def format_windows_search_results(results: List, search_type: str) -> None:
    """
    Formats and displays search results with Windows-specific information.
    Shows file sizes, paths, and optional attribute statistics.

    Args:
        results (List): Search results from find functions.
        search_type (str): Type of search performed:
        'pattern', 'extension', 'large', or 'system'.

    Returns:
        None: Outputs results to console.
    """
    if not results:
        print(f'{ru.NOTHING_FOUND}')
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
        print(f'{ru.FORMATTING_ERROR}')

    try:
        base = results[0] if isinstance(results[0], str) else results[0]['path']
        parent = os.path.dirname(base)
        if parent:
            stats = analysis.get_windows_file_attributes_stats(parent)
            print(f'\n{ru.ATTRIBUTES_HEADER}:')
            for k, v in stats.items():
                print(f'    {k}: {v}')
    except Exception:
        pass

