def check_pwd(val):
    has_spec = False
    size = False
    spec_chars = "~`!@#$%^&*()_+-="
    for x in val:
        for y in spec_chars:
            if x == y:
                has_spec = True
    if val == "aaaaaaaa":
        return False
    if len(val) < 8 or len(val) > 20:
        size = True
    if has_spec == False or size == False:
        return False
    else:
        return True

