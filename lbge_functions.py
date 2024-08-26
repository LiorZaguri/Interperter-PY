import numbers

"""
Adds two elements together based on their types.

- If both `x` and `y` are numbers, returns their sum.
- If both `x` and `y` are strings, concatenates them.
- If `x` is a list and `y` is a list, concatenates the lists. If `y` is not a list, appends `y` to `x`.
- If both `x` and `y` are tuples, concatenates them.
- If both `x` and `y` are sets, returns their union.
- If `x` is a string and `y` is a number (or vice versa), concatenates them as strings.

"""


def ADD(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        return x + y
    elif isinstance(x, str) and isinstance(y, str):
        return x + y
    elif isinstance(x, list):
        if isinstance(y, list):
            return x + y
        else:
            x.append(y)
            return x
    elif isinstance(x, tuple) and isinstance(y, tuple):
        return x + y
    elif isinstance(x, set) and isinstance(y, set):
        return x | y
    elif (isinstance(x, str) and isinstance(y, numbers.Number)) or (
            isinstance(x, numbers.Number) and isinstance(y, str)):
        return str(x) + str(y)
    elif isinstance(x, str):
        try:
            return x + ''.join(y)
        except TypeError:
            return x + str(y)
    else:
        raise ValueError(f"Unsupported types or mismatched types {type(x)} and {type(y)}")


"""
    Subtracts one element from another based on their types.

    - If both `x` and `y` are numbers, returns their difference.
    - If both `x` and `y` are lists, returns a list with elements of `y` removed from `x`.
    - If both `x` and `y` are sets, returns the difference of the sets.

"""


def SUB(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        return x - y
    elif isinstance(x, list) and isinstance(y, list):
        return [item for item in x if item not in y]
    elif isinstance(x, set) and isinstance(y, set):
        return x - y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Multiplies two elements together based on their types.

- If both `x` and `y` are numbers, returns their product.
- If `x` is a string and `y` is an integer (or vice versa), returns the string repeated `y` times.
- If `x` is a list and `y` is an integer (or vice versa), returns the list repeated `y` times.

"""


def MUL(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        return x * y
    elif isinstance(x, str) and isinstance(y, numbers.Integral) or \
            isinstance(x, numbers.Integral) and isinstance(y, str):
        return x * y
    elif isinstance(x, list) and isinstance(y, numbers.Integral) or \
            isinstance(x, numbers.Integral) and isinstance(y, list):
        return x * y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Divides one number by another.

- If both `x` and `y` are numbers, returns the result of `x` divided by `y`.

Raises:
    ValueError: If `y` is zero or if the types of `x` and `y` are unsupported or mismatched.
"""


def DIVIDE(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        if y == 0:
            raise ValueError("Cannot divide by 0")
        return x / y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Performs floor division on two numbers.

- If both `x` and `y` are numbers, returns the result of `x` floor divided by `y`.

Raises:
    ValueError: If `y` is zero or if the types of `x` and `y` are unsupported or mismatched.
"""


def FLOOR_DIVIDE(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        if y == 0:
            raise ValueError("cannot divide by 0")
        return x // y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Raises a number to the power of another.

- If both `x` and `y` are numbers, returns `x` raised to the power of `y`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def POWER(x, y):
    if isinstance(x, numbers.Number) and isinstance(y, numbers.Number):
        return x ** y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the square of an integer.

- If `x` is an integer, returns `x` squared.

Raises:
    ValueError: If the type of `x` is unsupported or mismatched.
"""


def SQUARE(x):
    if isinstance(x, numbers.Integral):
        return x ** 2
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the factorial of an integer.

- If `x` is an integer, returns `x` factorial.

Raises:
    ValueError: If the type of `x` is unsupported or mismatched.
"""


def FACTORIAL(x):
    if isinstance(x, numbers.Integral):
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the absolute value of a number.

- If `x` is a number, returns its absolute value.

Raises:
    ValueError: If the type of `x` is unsupported or mismatched.
"""


def ABS(x):
    if isinstance(x, numbers.Integral) or isinstance(x, numbers.Real):
        return abs(x)
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the remainder of the division of two integers.

- If both `x` and `y` are integers, returns `x` modulo `y`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def MOD(x, y):
    if isinstance(x, numbers.Integral) and isinstance(y, numbers.Integral):
        return x % y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the square root of a number.

- If `x` is a number, returns its square root.

Raises:
    ValueError: If the type of `x` is unsupported or mismatched.
"""


def SQRT(x):
    if isinstance(x, numbers.Number):
        return POWER(x, 0.5)
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the minimum of two elements.

- If both `x` and `y` are integers or strings, returns the smaller one.
- If both `x` and `y` are lists, returns the shorter list.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def MIN(x, y):
    if isinstance(x, numbers.Integral) and isinstance(y, numbers.Integral):
        return min(x, y)
    elif isinstance(x, str) and isinstance(y, str):
        return min(x, y)
    elif isinstance(x, list) and isinstance(y, list):
        return x if len(x) < len(y) else y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Returns the maximum of two elements.

- If both `x` and `y` are integers or strings, returns the larger one.
- If both `x` and `y` are lists, returns the longer list.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def MAX(x, y):
    if isinstance(x, numbers.Integral) and isinstance(y, numbers.Integral):
        return max(x, y)
    elif isinstance(x, str) and isinstance(y, str):
        return max(x, y)
    elif isinstance(x, list) and isinstance(y, list):
        return x if len(x) > len(y) else y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Assigns the value of `y` to `x`.

- If `x` and `y` are of the same type, assigns `y` to `x` and returns `x`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def ASSIGN(x, y):
    if isinstance(x, type(y)):
        x = y
        return x
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Checks if two elements are equal.

- If `x` and `y` are of the same type, returns `True` if they are equal, `False` otherwise.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def EQUAL(x, y):
    if isinstance(x, type(y)):
        return x == y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Checks if two elements are not equal.

- Returns the logical negation of `EQUAL(x, y)`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def NOT_EQUAL(x, y):
    return NOT(EQUAL(x, y))


"""
Checks if `x` is greater than `y`.

- If `x` and `y` are of the same type, returns `True` if `x` is greater, `False` otherwise.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def GREATER(x, y):
    if isinstance(x, type(y)):
        return x > y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Checks if `x` is greater than or equal to `y`.

- Returns the logical OR of `GREATER(x, y)` and `EQUAL(x, y)`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def GREATER_EQUAL(x, y):
    return OR(GREATER(x, y), EQUAL(x, y))


"""
Checks if `x` is smaller than `y`.

- Returns the logical negation of `GREATER_EQUAL(x, y)`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def SMALLER(x, y):
    return NOT(GREATER_EQUAL(x, y))


"""
Checks if `x` is smaller than or equal to `y`.

- Returns the logical OR of `SMALLER(x, y)` and `EQUAL(x, y)`.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def SMALLER_EQUAL(x, y):
    return OR(SMALLER(x, y), EQUAL(x, y))


"""
Performs a logical OR operation.

- If both `x` and `y` are booleans, returns `True` if either `x` or `y` is `True`, `False` otherwise.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def OR(x, y):
    if isinstance(x, bool) and isinstance(y, bool):
        return x or y
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Performs a logical AND operation.

- If both `x` and `y` are booleans, returns `True` if both `x` and `y` are `True`, `False` otherwise.

Raises:
    ValueError: If the types of `x` and `y` are unsupported or mismatched.
"""


def AND(x, y):
    if isinstance(x, bool) and isinstance(y, bool):
        return x and y
    else:
        raise ValueError("Unsupported types or mismatched types1")


"""
Performs a logical NOT operation.

- If `x` is a boolean, returns the logical negation of `x`.

Raises:
    ValueError: If the type of `x` is unsupported or mismatched.
"""


def NOT(x):
    if isinstance(x, bool):
        return not x
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Removes an element from a list by its index.

- If `arr` is a list and `index` is an integer, removes and returns the element at `index` in `arr`.

Raises:
    ValueError: If `arr` is not a list or `index` is not an integer.
"""


# EXTRA FUNCTIONS FOR ARRAYS
def REMOVE(arr, index):
    if isinstance(arr, list) and isinstance(index, numbers.Integral):
        return arr.pop(index)
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Appends an object to a list.

- If `arr` is a list, appends `obj` to the end of `arr` and returns the updated list.

Raises:
    ValueError: If `arr` is not a list.
"""


def APPEND(arr, obj: object):
    if isinstance(arr, list):
        arr.append(obj)
        return arr
    else:
        raise ValueError("The input is not a list")


"""
Splits a string into a list of substrings based on a separator.

- If `text` is a string, splits it into a list of substrings using the given `separator`.
- If no separator is provided, splits the string by whitespace.

Raises:
    ValueError: If `text` is not a string.
"""


# EXTRA FUNCTIONS FOR STRINGS
def SPLIT(text, separator=None):
    if isinstance(text, str):
        if separator is not None:
            str_after_split = text.split(separator)
        else:
            str_after_split = text.split()
        return str_after_split
    else:
        raise ValueError("The input is not a string")


"""
Replaces occurrences of a substring within a string.

- If `text`, `old`, and `new` are strings, returns a new string where all occurrences of `old` are replaced with `new`.

Raises:
    ValueError: If any of `text`, `old`, or `new` is not a string.
"""


def REPLACE(text, old, new):
    if isinstance(text, str) and isinstance(old, str) and isinstance(new, str):
        return text.replace(old, new)
    else:
        raise ValueError("The input is not a string")


"""
Returns the length of an object.

- Returns the length of `self`, which can be a string, list, tuple, or other collection.

Raises:
    TypeError: If `self` does not support the `len()` function.
"""


def LENGTH(self):
    return len(self)


"""
Checks if an element is in a collection.

- If `collection` is a string, list, tuple, or set, returns `True` if `element` is found in `collection`, `False` otherwise.

Raises:
    ValueError: If `collection` is not a string, list, tuple, or set, or if `element` is not of the appropriate type for the collection.
"""


def CONTAINS(collection, element):
    if isinstance(collection, str):
        if not isinstance(element, str):
            raise ValueError("The input is not a string")
    elif isinstance(collection, (list, tuple, set)):
        pass
    else:
        raise ValueError("The input is not a string")

    return element in collection


"""
Returns the index of the first occurrence of an element in a collection.

- If `collection` is a string, list, or tuple, returns the index of `element` in `collection`.
- If `collection` is a set, converts it to a list and then finds the index of `element`.

Raises:
    ValueError: If `element` is not found in `collection` or if `collection` is not a string, list, tuple, or set.
"""


def INDEX(collection, element):
    if isinstance(collection, (str, list, tuple)):
        if element in collection:
            return collection.index(element)
        else:
            raise ValueError("The element is not in the collection")
    elif isinstance(collection, set):
        collection_list = list(collection)
        if element in collection_list:
            return collection_list.index(element)
        else:
            raise ValueError("The element is not in the collection")
    else:
        raise ValueError("The collection must be a string, list, tuple or set")


"""
Checks if all alphabetic characters in a string are uppercase.

- If `text` is a string, returns `True` if all alphabetic characters are uppercase, `False` otherwise.

Raises:
    ValueError: If `text` is not a string.
"""


def ISUPPER(text):
    if isinstance(text, str):
        return text.isupper()
    else:
        raise ValueError("the input is not string")


"""
Checks if all alphabetic characters in a string are lowercase.

- If `text` is a string, returns `True` if all alphabetic characters are lowercase, `False` otherwise.

Raises:
    ValueError: If `text` is not a string.
"""


def ISLOWER(text):
    if isinstance(text, str):
        return text.islower()
    else:
        raise ValueError("the input is not string")


"""
Concatenates two strings.

- Uses the `ADD()` function to concatenate `word` and `text`.

Raises:
    ValueError: If the types of `word` and `text` are unsupported or mismatched.
"""


def CONCAT(word, text):
    return ADD(word, text)


"""
Reverses a string.

- If `text` is a string, returns a new string that is the reverse of `text`.

Raises:
    ValueError: If `text` is not a string.
"""


def REVERSE(text):
    if isinstance(text, str):
        return text[::-1]
    else:
        raise ValueError("the input is not string")


def GET(collection, index):
    if isinstance(collection, (list, tuple)) and isinstance(index, numbers.Integral):
        try:
            return collection[index]
        except IndexError:
            raise ValueError("Index out of range")
    else:
        raise ValueError("Unsupported types or mismatched types")


"""
Prints the provided text.

- Prints the value of `text` to the standard output.

Raises:
    ValueError: If `text` is not a string.
"""


def PRINT(text):
    if isinstance(text, str) and "\\n" in text:
        text = text.replace("\\n", "\n")
    print(text)
