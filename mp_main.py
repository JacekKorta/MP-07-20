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


def main(quantity: int):
    if input_data_validator(quantity):
        pass
    else:
        return 'Input data should be an integer in the range 1-100'






