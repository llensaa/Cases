import os
import platform
from pathlib import Path
from typing import Union, List, Tuple
import ctypes

PathString = Union[str, Path]

FILE_ATTRIBUTE_HIDDEN = 0x02

INVALID_FILE_ATTRIBUTES = 0xFFFFFFFF


def is_windows_os() -> bool:
    if platform.system() == 'Windows':
        return True
    return False


def validate_windows_path(path: PathString) -> Tuple[bool, str]:
    path = str(path)

    p = Path(path)

    symbols_excepted = set(':/*?"<>|')

    for part in path:
        if part in symbols_excepted:
            return False, f'Путь содержит запрещённый символ'

    if len(path) > 260:
        return False, 'Длина пути превышает 260 символов'

    if not p.exists():
        return False, 'Пути не существует'

    return True, ''


def format_size(size_bytes: int) -> str:
    if size_bytes < 1000:
        return f'{size_bytes} B'

    if size_bytes < 1_000_000:
        return f'{size_bytes / 1000:.1f} KB'

    if size_bytes < 1_000_000_000:
        return f'{size_bytes / 1_000_000:.1f} MB'

    return f'{size_bytes / 1_000_000_000:.1f} GB'


def get_parent_path(path: PathString) -> str:
    path = str(path)
    return os.path.dirname(path)


def safe_windows_listdir(path: PathString) -> List[str]:
    try:
        return os.listdir(path)

    except (PermissionError, FileNotFoundError, OSError):
        return []


def is_hidden_windows_file(path: str) -> bool:
    attrs = ctypes.windll.kernel32.GetFileAttributesW(path)
    if attrs == INVALID_FILE_ATTRIBUTES:
        return False
    return bool(attrs & FILE_ATTRIBUTE_HIDDEN)
