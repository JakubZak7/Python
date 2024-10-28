def isPalindrome(text):
    print(text[::-1])
    if text == text[::-1]:
        return True
    else:
        return False

print(isPalindrome("kajak"))