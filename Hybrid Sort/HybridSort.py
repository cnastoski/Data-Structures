def merge_sort(unsorted, threshold, reverse):
    """
    Splits a list in half until it cant anymore, then merges them back together in order
    :param unsorted: the unsorted list
    :param threshold: if the list size is at or below the threshold, switch to insertion sort
    :param reverse: sorts the list in descending order if True
    :return: A sorted list
    """
    size = len(unsorted)
    if size < 2:
        return unsorted
    mid = size // 2
    first = unsorted[:mid]
    second = unsorted[mid:]
    if mid <= threshold:
        first = insertion_sort(first, reverse)
        second = insertion_sort(second, reverse)
        merged = merge(first, second, reverse)
        return merged
    else:
        first = merge_sort(first, threshold, reverse)
        second = merge_sort(second, threshold, reverse)
        merged = merge(first, second, reverse)
        return merged


def merge(first, second, reverse):
    """
    non-recursive part of merge_sort. takes two lists and merges them together in the right order
    :param first: first part of list
    :param second: second part of list
    :param reverse: sorts the list in descending order if True
    :return: the correctly merged list
    """
    temp = [0] * len(first + second)
    i = j = 0
    if reverse is False:
        while i + j < len(temp):
            if j == len(second) or (i < len(first) and first[i] < second[j]):
                temp[i + j] = first[i]
                i += 1
            else:
                temp[i + j] = second[j]
                j += 1
    else:
        while i + j < len(temp):
            if j == len(second) or (i < len(first) and first[i] > second[j]):
                temp[i + j] = first[i]
                i += 1
            else:
                temp[i + j] = second[j]
                j += 1
    return temp


def insertion_sort(unsorted, reverse):
    """
    Sorts a list using insertion sort
    :param unsorted: the list to sort
    :param reverse: true if list is to be sorted backwards
    :return: the sorted list
    """
    for i in range(1, len(unsorted)):
        j = i
        if not reverse:
            while j > 0 and unsorted[j] <= unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                j -= 1
        else:
            while j > 0 and unsorted[j] >= unsorted[j - 1]:
                unsorted[j], unsorted[j - 1] = unsorted[j - 1], unsorted[j]
                j -= 1
    return unsorted
