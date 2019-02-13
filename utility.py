from typing import Tuple, List

def extract_words_and_integers_from_string(aString: str) -> Tuple[List[str],List[int]]:
    words: List[str] = []
    integers: List[int] = []
    n: int = len(aString)
    i: int = 0
    while i < n:
        if(aString[i] >= "A" and aString[i] <= "Z" ) or (aString[i] >= "a" and aString[i] <= "z" ):
            w: str = aString[i]
            i += 1
            while i < n and ((aString[i] >= "A" and aString[i] <= "Z" ) or (aString[i] >= "a" and aString[i] <= "z" )):
                w += aString[i]
                i += 1
            words.append(w)
        elif aString[i] >= "0" and aString[i] <= "9" :
            number = int(aString[i])
            i += 1
            while i < n and (aString[i] >= "0" and aString[i] <= "9"):
                number = number*10 + int(aString[i])
                i += 1
            integers.append(number)
        else:
            i += 1
    return words, integers

def cardinal_to_2d_cartesian_coordinates(string: str) -> List[int]:
    (cardinal, coordinate) = extract_words_and_integers_from_string(string)
    assert len(cardinal) == 2 and len(coordinate) == 2
    coordinate[0], coordinate[1] = coordinate[1], coordinate[0]
    if cardinal[0] == "N":
        pass
    elif cardinal[0] == "S":
        coordinate[1] *= -1
    else:
        raise Exception("Format not supported for string: "+string)
    if cardinal[1] == "E":
        pass
    elif cardinal[1] == "W":
        coordinate[0] *= -1
    else:
        raise Exception("Format not supported for string: "+string)
    return coordinate

def time_traveled_by_drone_in_minutes(start: List[int], end: List[int], speed: List[int]) -> int:
    assert len(start) == 2 and len(end) == 2 and len(speed) == 2
    assert speed[0] > 0 and speed[1] > 0  # assumption
    return abs(end[0] - start[0])/speed[0] + abs(end[1] - start[1])/speed[1]

def determine_customer_promoter_detractor_rating(delta):
    """hard coded window definition of promoter/detractor rating"""
    assert delta.days >= 0
    if delta.seconds < (90 * 60):
        return "promoter"
    elif delta.seconds < (225 * 60):
        return "neutral"
    else:
        return "detractor"