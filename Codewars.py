# ======================================
# Solution 1: Even or Odd
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe
# ======================================
def even_or_odd(number):
    """Return 'Even' if the number is even, otherwise 'Odd'."""
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# ======================================
# Solution 2: Convert a Number to a String
# https://www.codewars.com/kata/5265326f5fda8eb1160004c8
# ======================================
def number_to_string(num):
    """Convert a number into a string."""
    return str(num)


# ======================================
# Solution 3: Remove String Spaces
# https://www.codewars.com/kata/57eae20f5500ad98e50002c5
# ======================================
def no_space(x):
    """Remove all spaces from the string."""
    return x.replace(" ", "")


# ======================================
# Solution 4: Vowel Count
# https://www.codewars.com/kata/54ff3102c1bad923760001f3
# ======================================
def get_count(string):
    """Return the number of vowels in the string."""
    vowels = 'aeiou'
    return sum(1 for char in string if char in vowels)
