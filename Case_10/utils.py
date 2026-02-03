import os
import platform
from pathlib import Path
from typing import Union, List, Tuple
import ctypes
import ru_local as ru

PathString = Union[str, Path]

FILE_ATTRIBUTE_HIDDEN = 0x02

INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF

FILE_ATTRIBUTE_SYSTEM = 0x4

FILE_ATTRIBUTE_READONLY = 0x1


def is_windows_os() -> bool:
    """
    Checks if the current operating system is Windows.
    
    Returns:
        bool: True if running on Windows, False otherwise.
    """
    if platform.system() == 'Windows':
        return True
    return False


def validate_windows_path(path: PathString) -> Tuple[bool, str]:
    """
    Validates a Windows filesystem path for correctness and accessibility.
    Checks for forbidden characters, path length limits, and existence.
    
    Args:
        path (Union[str, Path]): Path to validate.
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message) where is_valid is True 
        if path is valid, error_message contains description if invalid.
    """
    path = str(path)

    p = Path(path)

    symbols_excepted = set(':/*?"<>|')

    for part in path:
        if part in symbols_excepted:
            return False, f'{ru.PATH_CONTAINS_FORBIDDEN_CHAR}'

    if len(path) > 260:
        return False, f'{ru.PATH_TOO_LONG_ERROR}'

    if not p.exists():
        return False, f'{ru.PATH_DOES_NOT_EXIST}'

    return True, ''


def format_size(size_bytes: int) -> str:
    """
    Formats file size in bytes to human-readable string.
    Uposes standard units: B, KB, MB, GB.
    
    Args:
        size_bytes (int): File size in bytes.
    
    Returns:
        str: Formatted size string (e.g., "1.5 MB", "256 B").
    """
    if size_bytes < 1000:
        return f'{size_bytes} B'

    if size_bytes < 1_000_000:
        return f'{size_bytes / 1000:.1f} KB'

    if size_bytes < 1_000_000_000:
        return f'{size_bytes / 1_000_000:.1f} MB'

    return f'{size_bytes / 1_000_000_000:.1f} GB'


def get_parent_path(path: PathString) -> str:
    """
    Gets the parent directory path of a given path.
    
    Args:
        path (Union[str, Path]): Original file or directory path.
    
    Returns:
        str: Parent directory path.
    """
    path = str(path)
    return os.path.dirname(path)


def safe_windows_listdir(path: PathString) -> List[str]:
    """
    Safely lists directory contents, handling permission and access errors.
    
    Args:
        path (Union[str, Path]): Directory path to list.
    
    Returns:
        List[str]: List of file and directory names, or empty list on error.
    """
    try:
        return os.listdir(path)

    except (PermissionError, FileNotFoundError, OSError):
        return []


def is_hidden_windows_file(path: str) -> bool:
    """
    Checks if a file or directory has the hidden attribute in Windows.
    
    Args:
        path (str): Path to check.
    
    Returns:
        bool: True if file is hidden, False otherwise or on error.
    """
    attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
    if attrs == INVALID_FILE_ATTRIBUTES:
        return False
    return bool(attrs & FILE_ATTRIBUTE_HIDDEN)


def is_system_windows_file(path: PathString) -> bool:
    """
    Checks if a file or directory has the system attribute in Windows.
    
    Args:
        path (Union[str, Path]): Path to check.
    
    Returns:
        bool: True if file is a system file, False otherwise or on error.
    """
    attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
    if attrs == INVALID_FILE_ATTRIBUTES:
        return False

    return bool(attrs & FILE_ATTRIBUTE_SYSTEM)


def is_readonly_windows_file(path: PathString) -> bool:
    """
    Checks if a file or directory has the read-only attribute in Windows.
    
    Args:
        path (Union[str, Path]): Path to check.
    
    Returns:
        bool: True if file is read-only, False otherwise or on error.
    """
    attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
    if attrs == INVALID_FILE_ATTRIBUTES:
        return False

    return bool(attrs & FILE_ATTRIBUTE_READONLY)
    
