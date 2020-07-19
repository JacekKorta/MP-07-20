from typing import Tuple


def input_data_validator(input_data) -> bool:
    if isinstance(input_data, int) and 1 <= input_data <= 100:
        return True
    else:
        return False


def count_large_boxes(quantity: int) -> Tuple[int, int]:
    large = quantity // 9
    rest = quantity % 9
    if rest > 6:
        large += 1
        rest = 0
    return large, rest


def count_medium_boxes(rest_from_large: int) -> int:
    if rest_from_large:
        medium = rest_from_large // 6
        rest = rest_from_large % 6
        if rest > 3:
            medium += 1
        return medium
    else:
        return 0


def main(quantity: int):
    if input_data_validator(quantity):
        pass
    else:
        return 'Input data should be an integer in the range 1-100'






