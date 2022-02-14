def check_pwd(val):
    has_spec = False
    size = False
    has_upper = False
    has_lower = False
    has_digit = False
    spec_chars = "~`!@#$%^&*()_+-="
    for x in val:
        if x.isupper():
            has_upper = True
        if x.islower():
            has_lower = True
        if x.isdigit():
            has_digit = True
        for y in spec_chars:
            if x == y:
                has_spec = True
    if 7 < len(val) < 21:
        size = True
    if has_spec == False or size == False or has_upper == False or has_lower == False or has_digit == False:
        return False
    else:
        return True

