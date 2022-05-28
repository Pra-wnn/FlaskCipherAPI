from collections import deque
import string


def ceaser(rotate_string, number_to_rotate_by):

    upper = deque(string.ascii_uppercase)
    lower = deque(string.ascii_lowercase)

    upper.rotate(-number_to_rotate_by)  #-ve infront matches the other cipher placemeent check
    
    lower.rotate(-number_to_rotate_by)

    upper = ''.join(list(upper))
    lower = ''.join(list(lower))

    return rotate_string.translate(upper.maketrans(string.ascii_uppercase, upper)).translate(lower.maketrans(string.ascii_lowercase,lower))


