def list_divide(numbers, divide=2):
    clean_count = 0
    for number in numbers:
        if number % divide == 0:
            clean_count += 1
    return clean_count


class ListDivideException(Exception):
    pass


def test_list_divide(numbers, divide=2):
    try:
        list_divide(numbers, divide)
    except:
        raise ListDivideException


test_list_divide([1,2,3,4,5])
test_list_divide([])
test_list_divide([2,4,6,8,10])
test_list_divide([30,54,63,98,100], divide=10)
test_list_divide([1,2,3,4,5], divide=1)
test_list_divide([7, "a"])