# Exercise 3
# Given a simple quote (string) with some numeric characters -
# we would like a function that removes all numeric characters

# Extension: Can you replace all numeric characters for their
# corresponding string, for example ('1' --> 'one', '12' --> twelve)
# This solution only needs to work for value less than 100.
# Some starter code is provided for you.

# Further extension: Use your working numericToAlpha function to
# update of replace removeNumeric with a replaceNumeric function.
# This function should turn the following into the subsequent string.
# "I have 1 deck of cards with 4 suits and 13 values, making 52 cards all together." -->
# "I have one deck of cards with four suits and thirteen values, making fifty-two cards all together."

quote = " I have 1 deck of cards with 4 suits and 13 values, making 52 cards all together."


def remove_numeric(input_str: str) -> str:
    valid_words = []
    for word in input_str.split():
        if word.isnumeric():
            word = numeric_to_alpha(int(word))
        valid_words.append(word)

    return ' '.join(valid_words)


print(remove_numeric(quote))


# Extension code

def numeric_to_alpha(num: int) -> str:
    up_to_twenty = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                    'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
                    'nineteen', 'twenty']
    up_to_ninety = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if num <= 20:
        return up_to_twenty[num]

    prefix = int(num / 10) - 2
    suffix = num % 10

    if num % 10 == 0:
        return up_to_ninety[prefix]

    return up_to_ninety[prefix] + '-' + up_to_twenty[suffix]


def test_numeric_to_alpha() -> None:
    for i in range(0, 100, 3):
        print(str(i), '-->', numeric_to_alpha(i))


test_numeric_to_alpha()
