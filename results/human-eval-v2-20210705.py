

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """

    l = sorted(l)
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2.0


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
____________________________ [doctest] test.median _____________________________
004 Return median of elements in the list l.
005     >>> median([3, 1, 2, 4, 5])
006     3
007     >>> median([-10, 4, 6, 1000, 10, 20])
Expected:
    15.0
Got:
    8.0

/fs03/da33/terry/apieval/final_data/open-eval/test.py:7: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.median
============================== 1 failed in 0.38s ===============================


"""

##################################################


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """

    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - shift:] + s[:len(s) - shift]


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
________________________ [doctest] test.circular_shift _________________________
003 Circular shift the digits of the integer x, shift the digits right by shift
004     and return the result as a string.
005     If shift > number of digits, return digits reversed.
006     >>> circular_shift(12, 1)
Expected:
    "21"
Got:
    '21'

/fs03/da33/terry/apieval/final_data/open-eval/test.py:6: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.circular_shift
============================== 1 failed in 0.22s ===============================


"""

##################################################


def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return len(list(filter(lambda x: x > 0, [digits_sum(i) for i in arr])))


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
__________________________ [doctest] test.count_nums ___________________________
003 
004     Write a function count_nums which takes an array of integers and returns
005     the number of elements which has a sum of digits > 0.
006     If a number is negative, then its first signed digit will be negative:
007     e.g. -123 has signed digits -1, 2, and 3.
008     >>> count_nums([]) == 0
Expected nothing
Got:
    True

/fs03/da33/terry/apieval/final_data/open-eval/test.py:8: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.count_nums
============================== 1 failed in 0.24s ===============================


"""

##################################################


def odd_count(lst):
    """Given a list of strings, where each string consists of only digits, return a list.
    Each element i of the output should be "the number of odd elements in the
    string i of the input." where all the i's should be replaced by the number
    of odd digits in the i'th string of the input.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """

    res = []
    for arr in lst:
        n = sum(int(d)%2==1 for d in arr)
        res.append("the number of odd elements " + str(n) + "n the str"+ str(n) +"ng "+ str(n) +" of the "+ str(n) +"nput.")
    return res


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
___________________________ [doctest] test.odd_count ___________________________
003 Given a list of strings, where each string consists of only digits, return a list.
004     Each element i of the output should be "the number of odd elements in the
005     string i of the input." where all the i's should be replaced by the number
006     of odd digits in the i'th string of the input.
007 
008     >>> odd_count(['1234567'])
Expected:
    ["the number of odd elements 4n the str4ng 4 of the 4nput."]
Got:
    ['the number of odd elements 4n the str4ng 4 of the 4nput.']

/fs03/da33/terry/apieval/final_data/open-eval/test.py:8: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.odd_count
============================== 1 failed in 0.23s ===============================


"""

##################################################


def sort_array(arr):
    """
    In this Kata, you have to sort an array of non-negative integers according to
    number of ones in their binary representation in ascending order.
    For similar number of ones, sort based on decimal value.

    It must be implemented like this:
    >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
    >>> sort_array([-2, -3, -4, -5, -6]) == [-6, -5, -4, -3, -2]
    >>> sort_array([1, 0, 2, 3, 4]) [0, 1, 2, 3, 4]
    """

    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
__________________________ [doctest] test.sort_array ___________________________
003 
004     In this Kata, you have to sort an array of non-negative integers according to
005     number of ones in their binary representation in ascending order.
006     For similar number of ones, sort based on decimal value.
007 
008     It must be implemented like this:
009     >>> sort_array([1, 5, 2, 3, 4]) == [1, 2, 3, 4, 5]
Expected nothing
Got:
    False

/fs03/da33/terry/apieval/final_data/open-eval/test.py:9: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.sort_array
============================== 1 failed in 0.23s ===============================


"""

##################################################


def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """

    if not arr: return None
    prod = 0 if 0 in arr else (-1) ** len(list(filter(lambda x: x < 0, arr)))
    return prod * sum([abs(i) for i in arr])


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
__________________________ [doctest] test.prod_signs ___________________________
003 
004     You are given an array arr of integers and you need to return
005     sum of magnitudes of integers multiplied by product of all signs
006     of each number in the array, represented by 1, -1 or 0.
007     Note: return None for empty arr.
008 
009     Example:
010     >>> prod_signs([1, 2, 2, -4]) == -9
Expected nothing
Got:
    True

/fs03/da33/terry/apieval/final_data/open-eval/test.py:10: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.prod_signs
============================== 1 failed in 0.22s ===============================


"""

##################################################


def order_by_points(nums):
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    >>> order_by_points([]) == []
    """

    def digits_sum(n):
        neg = 1
        if n < 0: n, neg = -1 * n, -1 
        n = [int(i) for i in str(n)]
        n[0] = n[0] * neg
        return sum(n)
    return sorted(nums, key=digits_sum)


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
________________________ [doctest] test.order_by_points ________________________
003 
004     Write a function which sorts the given list of integers
005     in ascending order according to the sum of their digits.
006     Note: if there are several items with similar sum of their digits,
007     order them based on their index in original list.
008 
009     For example:
010     >>> order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
Expected nothing
Got:
    True

/fs03/da33/terry/apieval/final_data/open-eval/test.py:10: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.order_by_points
============================== 1 failed in 0.25s ===============================


"""

##################################################


def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """

    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    res = ''
    while number: 
        div = number // num[i] 
        number %= num[i] 
        while div: 
            res += sym[i] 
            div -= 1
        i -= 1
    return res.lower()


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
_______________________ [doctest] test.int_to_mini_roman _______________________
003 
004     Given a positive integer, obtain its roman numeral equivalent as a string,
005     and return it in lowercase.
006     Restrictions: 1 <= num <= 1000
007 
008     Examples:
009     >>> int_to_mini_roman(19) == 'xix'
Expected nothing
Got:
    True

/fs03/da33/terry/apieval/final_data/open-eval/test.py:9: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.int_to_mini_roman
============================== 1 failed in 0.34s ===============================


"""

##################################################


def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """

    import hashlib
    return hashlib.md5(text.encode('ascii')).hexdigest() if text else None


"""

============================= test session starts ==============================
platform linux -- Python 3.8.3, pytest-8.1.1, pluggy-1.4.0
rootdir: /fs03/da33/terry/apieval/final_data/open-eval
plugins: anyio-4.2.0, Faker-21.0.0, pyfakefs-5.4.1
collected 1 item

test.py F                                                                [100%]

=================================== FAILURES ===================================
_________________________ [doctest] test.string_to_md5 _________________________
003 
004     Given a string 'text', return its md5 hash equivalent string.
005     If 'text' is an empty string, return None.
006 
007     >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
Expected nothing
Got:
    True

/fs03/da33/terry/apieval/final_data/open-eval/test.py:7: DocTestFailure
=========================== short test summary info ============================
FAILED test.py::test.string_to_md5
============================== 1 failed in 0.25s ===============================


"""

##################################################

