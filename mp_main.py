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


def count_small_boxes(rest_from_medium: int) -> int:
    if rest_from_medium:
        small = rest_from_medium // 3
        rest = rest_from_medium % 3
        if rest:
            small += 1
        return small
    else:
        return 0


def count_bulk_boxes(boxes: dict) -> int:
    all_boxes = sum(boxes.values())
    bulk = all_boxes // 3
    if all_boxes % 3 > 0 and all_boxes > 1:
        bulk += 1
    return bulk


def check_is_it_exception(quantity: int) -> bool:
    if 9 < quantity < 16:
        return True
    return False


def packing_exception(quantity: int) -> dict:
    """The simplest way to handle specific packing for items "A" in the range 10-15 based on customer specification"""
    if quantity < 13:
        return {'small': 0, 'medium': 2, 'large': 0, 'bulk': 1}
    else:
        return {'small': 0, 'medium': 0, 'large': 2, 'bulk': 1}


def main(quantity: int):
    if input_data_validator(quantity):
        if check_is_it_exception(quantity):
            boxes = packing_exception(quantity)
        else:
            boxes = {'small': 0, 'medium': 0, 'large': 0, 'bulk': 0}
            boxes['large'], rest = count_large_boxes(quantity)
            if rest > 3:
                boxes['medium'] = count_medium_boxes(rest)
            else:
                boxes['small'] = count_small_boxes(rest)
            boxes['bulk'] = count_bulk_boxes(boxes)
        return boxes
    else:
        return 'Input data should be an integer in the range 1-100'





