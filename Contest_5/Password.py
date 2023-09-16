def check_password(password):
    if len(password) < 8:
        return False
    lowercase_bool = False
    uppercase_bool = False
    digit_bool = False
    for char in password:
        if char.islower():
            lowercase_bool = True
        elif char.isupper():
            uppercase_bool = True
        elif char.isdigit():
            digit_bool = True

    if not (lowercase_bool and uppercase_bool and digit_bool):
        return False

    unique_chars = set(password)
    if len(unique_chars) < 4:
        return False

    if "anna" in password.lower():
        return False

    return True


password = input()
if check_password(password):
    print("strong")
else:
    print("weak")
