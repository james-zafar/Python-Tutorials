# Exercise 10
# A palindrome is a word, number, phrase, or other sequence of characters which
# reads the same backward as forward
#  In this example the phrase "a bba" should be a valid palindrome if we ignore white space,
# but the function returns False. How can we fix this?

# Extension: Could we further extend this solution to ignore the case,
# such that "a bBa" is also considered a valid palindrome on line 24?
# Further Extension: "don't nod" is a valid palindrome but raises an
# exception on when we use this as input on line 26. Why is this?


def is_palindrome(phrase: str) -> bool:
    # Strip any whitespace and convert the input to lower case
    phrase = phrase.replace(' ', '').lower()
    # Next we should remove any punctuation
    phrase = [letter for letter in phrase if letter.isalpha() or letter.isdigit()]
    # We could also write this using a regular for loop
    # new_phrase = ''
    # for letter in phrase:
    #     if letter.isalpha():
    #         new_phrase = ''.join([new_phrase, letter])
    # return new_phrase == new_phrase[::-1]
    return phrase == phrase[::-1]


print(is_palindrome('now i won'))
# This should fail
print(is_palindrome('not one'))
print(is_palindrome('t'))
# a bba is a valid palindrome
print(is_palindrome('a bba'))
print(is_palindrome('was it a car or a cat i saw'))
# Extension
print(is_palindrome('a bBa'))
# Further extension - can we ignore punctuation to recognise palindromes
print(is_palindrome("don't nod"))
