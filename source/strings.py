#!python


def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == '':
        return True

    low_text = text.lower()
    low_pattern = pattern.lower()
    indexes = find_all_indexes_recursive(low_text, low_pattern, 0, 0, [], []) # O(n) complexity
    return len(indexes) > 0


# def contains_recursive(text, pattern, text_index=0, patt_index=0, found=[]):
#     # if indeces fall out of range, pattern does not exist
#     if text_index >= len(text) or patt_index >= len(pattern):
#         return False

#     # check if current text at t-index is equal to pattern at p-index
#     if text[text_index] == pattern[patt_index]:
#         found.append(text[text_index])
#         patt_index += 1
#     # if not, check if text at t-index is qual to pattern at 0 index
#     elif text[text_index] == pattern[0]:
#         found = [text[text_index]]
#         patt_index = 1
#     else:                               # otherwise, reset found array and pattern index
#         found = []
#         patt_index = 0

#     # if the found array matches the pattern, the pattern has been found!!
#     if ''.join(found) == pattern:
#         return True
#     else:  # otherwise, do a recursive call
#         return contains_recursive(text, pattern, text_index + 1, patt_index, found)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == '':
        return 0

    low_text = text.lower()
    low_pattern = pattern.lower()
    indexes = find_all_indexes_recursive(low_text, low_pattern, 0, 0, [], []) # O(n) complexity
    if len(indexes) > 0:
        return indexes[0]
    else:
        return None


# def find_index_recursive(text, pattern, text_index=0, patt_index=0, found=[]):
#     # if indeces fall out of range, pattern does not exist
#     if text_index >= len(text) or patt_index >= len(pattern):
#         return None

#     # check if current text at t-index is equal to pattern at p-index
#     if text[text_index] == pattern[patt_index]:
#         found.append(text[text_index])
#         patt_index += 1
#     # if not, check if text at t-index is qual to pattern at 0 index
#     elif text[text_index] == pattern[0]:
#         found = [text[text_index]]
#         patt_index = 1
#     else:                               # otherwise, reset found array and pattern index
#         found = []
#         patt_index = 0

#     # if the found array matches the pattern, the pattern has been found!!
#     if ''.join(found) == pattern:
#         return text_index - len(pattern) + 1
#     else:  # otherwise, do a recursive call
#         return find_index_recursive(text, pattern, text_index + 1, patt_index, found)


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    if pattern == '':
        return list(range(0, len(text)))

    low_text = text.lower()
    low_pattern = pattern.lower()
    return find_all_indexes_recursive(low_text, low_pattern, 0, 0, [], []) # O(n) complexity


def find_all_indexes_recursive(text, pattern, text_index=0, patt_index=0, found=[], found_indexes=[]):
    # if indeces fall out of range, pattern does not exist
    if text_index >= len(text) or patt_index >= len(pattern):
        return found_indexes

    # check if current text at t-index is equal to pattern at p-index
    if text[text_index] == pattern[patt_index]:
        found.append(text[text_index])
        patt_index += 1
    # if not, check if text at t-index is qual to pattern at 0 index
    elif text[text_index] == pattern[0]:
        found = [text[text_index]]
        patt_index = 1
    else:                               # otherwise, reset found array and pattern index
        found = []
        patt_index = 0

    # if the found array matches the pattern, the pattern has been found!!
    if ''.join(found) == pattern:
        found_indexes.append(text_index - len(pattern) + 1)
        if found [-1] == pattern[0] and len(pattern) > 1: # overlap edge case workaround
            found = [pattern[0]]
            patt_index = 1
        else:
            found = []
            patt_index = 0
        
    return find_all_indexes_recursive(text, pattern, text_index + 1, patt_index, found, found_indexes)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
