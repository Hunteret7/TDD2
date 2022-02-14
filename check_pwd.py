def check_pwd(val):
    has_spec = False
    size = False
    has_upper = False
    has_lower = False
    spec_chars = "~`!@#$%^&*()_+-="
    for x in val:
        if x.isupper():
            has_upper = True
        if x.islower():
            has_lower = True
        for y in spec_chars:
            if x == y:
                has_spec = True
    if val == "aaaaaaaa":
        return False
    if 7 < len(val) < 21:
        size = True
    if has_spec == False or size == False or has_upper == False or has_lower == False:
        return False
    else:
        return True

