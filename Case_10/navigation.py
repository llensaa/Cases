import os
from datetime import datetime
from typing import List, Dict, Any, Tuple
import utils



def get_current_drive() -> str:
    """
    Gets the current Windows drive letter from the working directory.

    Returns:
        str: Current drive letter with colon (e.g., "C:").
    """
    drive, rest = os.path.splitdrive(os.getcwd())
    return drive


def list_available_drives() -> List[str]:
    """
    Lists all available drives in the Windows system.

    Returns:
        List[str]: List of available drive letters with colons (e.g., ["C:", "D:"]).
    """
    # TODO: Вернуть список доступных дисков (['C:', 'D:', ...])
    # Использовать os.listdir('/') не подойдет для Windows!
    # Исследовать: использовать win32api или другие методы
    drives = os.listdrives()
    return drives


def list_directory(path: str) -> Tuple[bool, List[Dict[str, Any]]]:
    """
    Lists contents of a Windows directory with detailed file information.

    Args:
        path (str): Path to the directory to list.

    Returns:
        Tuple[bool, List[Dict[str, Any]]]: (success_status, items_list) where 
        items_list contains dictionaries with keys: 
        'name', 'type' ('file' or 'directory'), 'size' (in bytes), 
        'modified' (date string), 'hidden' (boolean).
    """
    try:
        items = utils.safe_windows_listdir(path)
        results = []

        for name in items:
            full_path = os.path.join(path, name)
            stat = os.stat(full_path)
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
    """
    Formats and displays directory contents with Windows-specific symbols.
    Shows hidden files with special markers and organized output.

    Args:
        items (List[Dict[str, Any]]): List of directory items from list_directory().
    """
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
    """
    Navigates to the parent directory in Windows filesystem.

    Args:
        current_path (str): Current directory path.

    Returns:
        str: Parent directory path, or empty string if navigation failed.
    """
    try:
        parent_path = utils.get_parent_path(current_path)
        if utils.validate_windows_path(parent_path):
            return parent_path
    except (OSError, PermissionError):
        return ''


def move_down(current_path: str, target_dir: str) -> Tuple[bool, str]:
    """
    Navigates into a specified subdirectory in Windows filesystem.

    Args:
        current_path (str): Current directory path.
        target_dir (str): Name of the subdirectory to enter.

    Returns:
        Tuple[bool, str]: (success_status, new_path) where success_status 
        is True if navigation succeeded, False otherwise.
    """
    try:
        if target_dir in utils.safe_windows_listdir(current_path):
            new_path = os.path.normpath(os.path.join(current_path, target_dir))

            if utils.validate_windows_path(new_path):
                return True, new_path

    except (PermissionError, OSError):
        return False, current_path


def get_windows_special_folders() -> Dict[str, str]:
    """
    Gets paths to Windows special folders for the current user.

    Returns:
        Dict[str, str]: Dictionary with folder names as keys and paths as values 
        (e.g., {'Desktop': 'C:\\Users\\...', 'Documents': '...'}).
    """
    userprofile = os.environ.get('USERPROFILE')
    if not userprofile:
        return {}

    special_folders = {
        'Desktop': os.path.join(userprofile, 'Desktop'),
        'Documents': os.path.join(userprofile, 'Documents'),
        'Downloads': os.path.join(userprofile, 'Downloads')
    }
    return special_folders

