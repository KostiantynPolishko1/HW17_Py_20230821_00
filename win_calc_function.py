def check_val_int(txt: str) -> int:

    if txt.find('.'):
        txt = txt.split(sep='.', maxsplit=-1)
    if txt[0].find(','):
        txt = txt[0].split(sep=',', maxsplit=-1)

    try:
        return abs(int(txt[0]))
    except ValueError:
        return 0


def check_win_min_max(value: int, _min: int, _max: int) -> int:

    if _min <= value <= _max:
        return value
    else:
        return _min if value < _min else _max
