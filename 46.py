#!/usr/bin/env python3

# 1. Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if­-then-­else construct available in Python.


def max(num1, num2):
    if num1 > num2 or num1 == num2:
        return num1
    else:
        return num2


# Test:
# print(max(3, 69))

# *********************************************************************

# 2. Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.


def max_of_three(num1, num2, num3):
    num_array = [num1, num2, num3]
    largest_num = 0

    for i in num_array:
        if i > largest_num:
            largest_num = i
    return largest_num


# Test:
# print(max_of_three(1, 2, 4))

# *********************************************************************

# 3. Define a function that computes the length of a given list or string. (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.) Please name your function length().


def length(item):
    length_count = 0

    for i in item:
        length_count += 1
    return length_count


# Test:
# print(length([1, 2, 3, 4, 5]))

# *********************************************************************

# 4. Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise. Please name your function is_vowel().


def is_vowel(char):
    return True if char.lower() in ["a", "e", "i", "o", "u"] else False


# Test:
# print(is_vowel("A"))

# *********************************************************************

# 5. Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). That is,
# double every consonant and place an occurrence of "o" in between.


def translate(initial_text):
    for char in initial_text:
        # if character is a vowel, print as is.
        if is_vowel(char):
            print(char, end="")
        # if character is a whitespace, print as is.
        elif char == " ":
            print(" ", end="")
        # if character is neither (i.e. is a consonant), print in rövarspråket.
        else:
            print(f"{char}o{char}", end="")
    print()


# Test:
# print(translate("this is fun"))

# *********************************************************************

# 6. Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers


def sum(list):
    sum = 0

    for item in list:
        sum += item

    return sum


def multiply(list):
    product = 1

    for item in list:
        product *= item

    return product


# Test:
# print(sum([1, 2, 3, 4]))
# print(multiply([1, 2, 3, 4]))

# *********************************************************************

# 7. Define a function reverse() that computes the reversal of a string.


def reverse(str):

    new_str = ""

    for i in range(len(str), 0, -1):
        new_str += str[i - 1]

    return new_str


# Test:
# print(reverse("hello"))

# *********************************************************************

# 8. Define a function is_palindrome() that recognizes palindromes.


def is_palindrome(word):
    return reverse(word) == word


# Test:
# print(is_palindrome("racecar"))

# *********************************************************************

# 9. Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and returns True if x is a member of a, False otherwise.


def is_member(value, value_list):
    for item in range(len(value_list)):
        if value == value_list[item]:
            return True
    return False


# Test
# print(is_member("x", ["a", "b", "x"]))

# *********************************************************************

# 10. Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.


def overlapping(list_a, list_b):
    for i in range(len(list_a)):
        for j in range(len(list_b)):
            if list_a[i] == list_b[j]:
                return True

    return False


# Test:
# print(overlapping([4, 5, 6, 2], [1, 2, 3]))

# *********************************************************************

# 11. Define a function generate_n_chars() that takes an integer n and a character c and returns a string, n characters long, consisting only of c:n.


def generate_n_chars(int, char):

    new_string = ""

    for i in range(int):
        new_string += char

    return new_string


# Test:
# print(generate_n_chars(6, "#"))

# *********************************************************************

# 12. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen


def histogram(int_list):
    for integer in int_list:
        print(integer * "*")


# Test:
# histogram([4, 9, 7])

# *********************************************************************

# 13. Write a function max_in_list() that takes a list of numbers and returns the largest one.


def max_in_list(num_list):

    largest_num = 0

    for num in num_list:
        if num > largest_num:
            largest_num = num

    return largest_num


# Test:
# print(max_in_list([3, 6, 8, 10, 96, 43, 2, 100, 15, 18, 204, 1]))

# *********************************************************************

# 14. Write a function words_to_integers() that maps a list of words into a list of integers representing the lengths of the correponding words


def words_to_integers(word_list):
    return [len(word) for word in word_list]


# Test:
# print(words_to_integers(["Hello", "world", "how", "may", "I", "help", "you"]))

# *********************************************************************

# 15. Write a function find_longest_word() that takes a list of words and returns the length of the longest one


def find_longest_word(word_list):

    longest_length = 0
    integer_list = words_to_integers(word_list)

    for item in integer_list:
        if item > longest_length:
            longest_length = item

    return longest_length


# Test:
# print(find_longest_word(["Hello", "world", "longword"]))

# *********************************************************************

# 16. Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.


def filter_long_words(word_list, n):

    filtered_list = []
    integer_list = words_to_integers(word_list)

    for i in range(len(integer_list)):
        if integer_list[i] > n:
            filtered_list.append(word_list[i])

    return filtered_list


# Test:
# print(filter_long_words(["Hello", "world", "longword"], 6))

# *********************************************************************

# 17. Write a function is_phrase_palindrome that accepts phrase palindromes.


def is_phrase_palindrome(phrase):
    return reverse(phrase.lower()) == phrase.lower()


# Test:
# print(is_phrase_palindrome("Step on no pets"))
