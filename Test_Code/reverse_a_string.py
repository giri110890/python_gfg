def check_palindrome(s):
    test = str(s)
    if str(test) == str(test[::-1]):
        print("Palindrome")
    else:
        print("not")


# Driver code
check_palindrome(111)
