def is_palindrome(value):
    str_value = str(value)
    str_value = str_value.replace(" ", "").lower()
    return str_value == str_value[::-1]

print(is_palindrome(121))
print(is_palindrome("racecar"))  