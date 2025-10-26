# Codewars
Codewars Journey
# ============================================
# Solution: Even or Odd
# ============================================

def even_or_odd(number):
    """
    Returns 'Even' if number is even, otherwise 'Odd'.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# ============================================
# Solution: Convert a Number to a String
# ============================================

def number_to_string(num):
    """
    Converts a number to a string.
    """
    return str(num)


# ============================================
# Solution: Remove String Spaces
# ============================================

def no_space(x):
    """
    Removes all spaces from the input string.
    """
    return x.replace(" ", "")


# ============================================
# Solution: Vowel Count
# ============================================

def get_count(sentence):
    """
    Returns the number of vowels (a, e, i, o, u) in a string.
    """
    vowels = 'aeiou'
    return sum(1 for char in sentence if char.lower() in vowels)
