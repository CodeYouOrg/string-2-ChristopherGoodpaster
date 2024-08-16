# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

def verbing(s):
    # +++your code here+++
def add_ing_or_ly(word):
    if len(word) < 3:
        return word
    if word.endswith('ing'):
        return word + 'ly'
    return word + 'ing'
    return
print(add_ing_or_ly('play'))    # Output will be 'playing'
print(add_ing_or_ly('playing')) # Output will be 'playingly'
print(add_ing_or_ly('do'))      # Output will be 'do'


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

def not_bad(s):
    # +++your code here+++
    def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    
    if not_index != -1 and bad_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index + 3:]
    
    return s
    
    return

print(not_bad('This dinner is not that bad!'))  # Output will be 'This dinner is good!'
print(not_bad('This movie is not so bad.'))     # Output will be 'This movie is good.'
print(not_bad('This is not bad at all!'))       # Output will be 'This is good at all!'
print(not_bad('This is bad, not good.'))        # Output will be 'This is bad, not good.'



# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
    # +++your code here+++
def split_string(s):
    mid = (len(s) + 1) // 2  # Determine the midpoint, adding 1 ensures the extra char goes to the front half if the length is odd.
    return s[:mid], s[mid:]   # Return the front and back halves as a tuple.

def front_back(a, b):
    a_front, a_back = split_string(a)  # Split string 'a' into front and back halves.
    b_front, b_back = split_string(b)  # Split string 'b' into front and back halves.
    return a_front + b_front + a_back + b_back  # Combine the halves in the specified order.

    return

print(front_back('abcd', 'xy'))    # Output will be 'abxcdy'
print(front_back('abcde', 'xyz'))  # Output will be 'abcxydez'
print(front_back('Kitten', 'Donut')) # Output will be 'KitDontenut'



# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')


if __name__ == '__main__':
    main()
