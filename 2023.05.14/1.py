def strong_password(password):
    length = len(password)
    if length < 8:
        return False
    elif length > 8:
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        for char in password:
            if char.isalpha():
                if char.isupper():
                    has_upper = True
                elif char.islower():
                    has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special = True
        if has_upper and has_lower and has_digit and has_special:
            return True
    else:
        return False

# >>> strong_password('aP3:kD_l3')
# True
# >>> strong_password('password')
# False

