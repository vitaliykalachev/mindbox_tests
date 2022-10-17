def get_label(num: int) -> int:
    assert isinstance(num, int), f"Expected numbers"
    assert num >= 0, f"Expected positive numbers"
    if num < 10:
        return num
    return num % 10 + get_label(num // 10)
