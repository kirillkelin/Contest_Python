def min_symbols_to_make_palindrome(s):
    def is_palindrome(string):
        return string == string[::-1]

    n = len(s)
    additions_left = 0
    for i in range(n):
        if is_palindrome(s[i:]):
            break
        else:
            additions_left += 1

    additions_right = 0
    for i in range(n - 1, -1, -1):
        if is_palindrome(s[:i + 1]):
            break
        else:
            additions_right += 1

    return min(additions_left, additions_right)


my_str = input()
print(min_symbols_to_make_palindrome(my_str))
