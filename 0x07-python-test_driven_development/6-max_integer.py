def max_integer(lst=None):
    """
    Find the maximum integer in a list of integers.

    If the list is empty or None, return None.
    """
    if lst is None or len(lst) == 0:
        return None
    return max(lst)

