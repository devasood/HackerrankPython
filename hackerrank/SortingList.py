import sys
from enum import Enum


def first_greater_than_second(first: float, second: float):
    return first > second


def first_smaller_than_second(first: float, second: float):
    return first < second


class SortingOperation(Enum):
    ASCENDING = first_smaller_than_second
    DESCENDING = first_greater_than_second


def find_second_last_index_without_sorting_entire_list_ignoring_duplicates(
        some_list: list, operation_type: SortingOperation = SortingOperation.ASCENDING):
    second_index, first_index = -sys.maxsize, some_list[0]
    if (operation_type(sys.maxsize, -sys.maxsize)):
        second_index = sys.maxsize

    for num in some_list:
        if operation_type(first_index, num):
            second_index = first_index
            first_index = num
        elif num != first_index and operation_type(second_index, num):
            second_index = num
    return second_index
