def human_file_size(byte_count: int, use_si: bool = True, precision: int = 2):
    if use_si:
        base = 1000
        units = ("kB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    else:
        base = 1024
        units = ("KiB", "MiB", "GiB", "TiB", "PiB", "EiB", "ZiB", "YiB")

    byte_count = abs(byte_count)
    unit = -1
    decimal_point = 10 ** precision

    if byte_count < base:
        return f"{byte_count} B"

    while round(byte_count * decimal_point) / decimal_point >= base and unit < len(units) - 1:
        byte_count /= base
        unit += 1

    return f"{round(byte_count, precision)} {units[unit]}"
