
def input_data_validator(input_data):
    if isinstance(input_data, int) and 1 <= input_data <= 100:
        return True
    else:
        return False


def fix_the_boxes(quantity: int) -> str:
    if input_data_validator(quantity):
        pass
    else:
        return 'Input data should be an integer in the range 1-100'
