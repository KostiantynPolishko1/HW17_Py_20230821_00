from window_data import *


class NoneValue(Exception):
    """value is empty"""
    pass


def check_val_int(txt: str) -> tuple:

    if txt.find('.'):
        txt = txt.split(sep='.', maxsplit=-1)
    if txt[0].find(','):
        txt = txt[0].split(sep=',', maxsplit=-1)

    try:
        if txt[0] == '':
            raise NoneValue('value is empty')
        return abs(int(txt[0])), True
    except NoneValue:
        return 0, True
    except ValueError:
        return 0, False


def check_win_min_max(value: int, _min: int, _max: int) -> int:

    if _min <= value <= _max:
        return value
    else:
        return _min if value < _min else _max


def check_combobox(key: str) -> bool:
    if key not in data:
        return True
    else:
        return False
