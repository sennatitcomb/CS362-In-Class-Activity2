import pytest
def palindrome(palindrome):
    x = len(palindrome)
    y = len(palindrome)
    x = int(x/2)
    count = 0
    j = y-1
    for i in range (0,x):
        if j > x:
            a = palindrome[i]
            b = palindrome[j]
            if a != b:
                return ("This is not a palindrome")
            j = j -1
    if count == 0:
        return("This is a palindrome")
def test_palindrome():
    assert palindrome("pony") == "This is not a palindrome"
def test_palindrome2():
    assert palindrome("madam") == "This is a palindrome"