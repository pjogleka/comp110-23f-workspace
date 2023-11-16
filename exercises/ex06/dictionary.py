"""Dictionary practice."""


__author__ = "730569615"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """Inverts a dict."""
    for key in dict1:
        i = 0
        while i < (len(dict1) - 1):
            vals = list(dict1.values())
            if vals[i] == vals[i + 1]:
                raise KeyError("Duplicate keys.")
            i += 1
    dict2 = {}
    for key, value in dict1.items():
        dict2[value] = key
    return dict2


def favorite_color(dict2: dict[str, str]) -> str:
    """Returns most popular color."""
    if len(dict2) == 0:
        return ""
    colors = list(dict2.values())
    counts = []
    i = 0
    for color in colors:
        count = 0
        for i in range(len(colors)):
            if color == colors[i]:
                count += 1
            i += 1
        counts.append(count)
    i = 0
    max = counts[i]
    for i in range(len(counts) - 1):
        if max < counts[i + 1]:
            max = counts[i + 1]
        i += 1
    if max == counts[0] and max == counts[1]:
        return colors[0]
    else:
        return colors[counts.index(max)]


def count(list1: list[str]) -> dict[str, int]:
    """Gives list counts."""
    dict1: dict[str, int] = {}
    for i in range(len(list1)):
        if list1[i] in dict1:
            dict1[list1[i]] += 1
        else:
            dict1[list1[i]] = 1
    return dict1


def alphabetizer(list1: list[str]) -> dict[str, list[str]]:
    """Alphabetized dictionary from list."""
    dict1: dict[str, list[str]] = {}
    for i in range(len(list1)):
        word = list1[i]
        letter = word[0].lower()
        if letter in dict1: 
            dict1[letter].append(word)
        else:
            dict1[letter] = []
            dict1[letter].append(word)
    return dict1


def update_attendance(dict1: dict[str, list[str]], day: str, student: str) -> dict[str, list[str]]:
    """Updates attendance."""
    update = dict1
    if day in update:
        update[day].append(student)
    else:
        update[day] = [student]
    return update