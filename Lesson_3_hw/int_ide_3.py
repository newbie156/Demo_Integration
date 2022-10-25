def palindrom():
    return rev_phrase == phrase[::-1]


phrase = input('Enter phrase: ')
rev_phrase = phrase[::-1]
if rev_phrase == phrase:
    print('The expression is a palindrome')
else:
    print('Try again')


palindrom()