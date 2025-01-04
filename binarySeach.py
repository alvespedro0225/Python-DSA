"""
Checks if the target element greater, smaller or equal to the middle element, discarding half of the collection appropriately or returning the value.
Can be recursive or iterative, with iterative having the advantage of using less memory due to function call stack.
Element type must support comparison.
"""

from typing import Any, Literal
from pydantic import NonNegativeInt

def BinarySearch(array: list[Any], key:Any) -> NonNegativeInt | Literal[-1]:
    """
    Looks for a particular element in a list of sorted elements and returns it's index if found and -1 if not found.\n
    Element must support ">" and "<" comparison.\n
    Iterative version.

    Args:
        array (list[Any]): List in which the element will be searched
        key (Any): Element to be searched

    Returns:
        int: Index of the element if it's on the list or -1 if it isn't.
    """
    high: NonNegativeInt = len(array) - 1
    low: NonNegativeInt = 0
    while low <= high:
        indexMid: NonNegativeInt = low + (high - low) // 2
        if key > array[indexMid]:
            low = indexMid + 1
        elif key < array[indexMid]:
            high = indexMid - 1
        else:
            return indexMid
    return -1