"""Test my zip function."""


__author__ = '730569615'


from lessons.zip import zip


def test_empty() -> None:
    """Test edge case of empty list."""
    assert zip([], []) == {}


def test_len1() -> None:
    """Test with length 1."""
    test_list1 = ['purple']
    test_list2 = [1]
    assert zip(test_list1, test_list2) == {'purple': 1}


def test_len2() -> None:
    """Test with length 2."""
    test_list1 = ['purple', 'blue']
    test_list2 = [1, 2]
    assert zip(test_list1, test_list2) == {'purple': 1, 'blue': 2}