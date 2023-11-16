"""Test my dict functions."""


__author__ = '730569615'


from exercises.ex06.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_len1() -> None:
    """Test invert with 1 key."""
    assert invert({'comp': '110'}) == {'110': 'comp'}


def test_invert_len2() -> None:
    """Test invert with 2 keys."""
    assert invert({'phys': '119', 'math': '383'}) == {'119': 'phys', '383': 'math'}


def test_invert_empty() -> None:
    """Test edge case of empty dict."""
    assert invert({}) == {}


def test_fav_color1() -> None:
    """Test fav color with 1 mode."""
    assert favorite_color({'Niko': 'black', 'Janie': 'blue', 'Saisha': 'blue'}) == 'blue'


def test_fav_color2() -> None:
    """Test fav color with 2 modes."""
    assert favorite_color({'Niko': 'black', 'Janie': 'blue', 'Saisha': 'blue', 'Blake': 'black'}) == 'black'


def test_fav_color_empty() -> None:
    """Test edge case of empty dict."""
    assert favorite_color({}) == ""


def test_count3() -> None:
    """Test count with 3 unique items."""
    assert count(['happy', 'sad', 'angry', 'angry']) == {'happy': 1, 'sad': 1, 'angry': 2}


def test_count4() -> None:
    """Test count with 4 unique items."""
    assert count(['happy', 'sad', 'angry', 'angry', 'excited', 'happy']) == {'happy': 2, 'sad': 1, 'angry': 2, 'excited': 1}


def test_count_empty() -> None:
    """Test count with an empty list."""
    assert count([]) == {}


def test_alphabetizer2() -> None:
    """Test alphabetizer with two items."""
    assert alphabetizer(['python', 'java']) == {'p': ['python'], 'j': ['java']}


def test_alphabetizer3() -> None:
    """Test alphabetizer with an three items."""
    assert alphabetizer(['python', 'java', 'puppy']) == {'p': ['python', 'puppy'], 'j': ['java']}


def test_alphabetizer_empty() -> None:
    """Test alphabetizer with an empty list."""
    assert alphabetizer([]) == {}


def test_update_attendance1() -> None:
    """Test update_attendance with empty starting list."""
    assert update_attendance({}, 'Tues', 'Niko') == {'Tues': ['Niko']}


def test_update_attendance() -> None:
    """Test update_attendance."""
    assert update_attendance({'Tues': ['Niko']}, 'Tues', 'Janie') == {'Tues': ['Niko', 'Janie']}


def test_update_attendance_empty() -> None:
    """Test update_attendance with empty args."""
    assert update_attendance({}, '', '') == {'': ['']}