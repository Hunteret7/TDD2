def check_pwd(val):
    has_spec = False
    size = False
    has_upper = False
    spec_chars = "~`!@#$%^&*()_+-="
    for x in val:
        if x.isupper():
            has_upper = True
            print("a")
        for y in spec_chars:
            if x == y:
                has_spec = True
                print("B")
    if val == "aaaaaaaa":
        return False
    if len(val) > 7 and len(val) < 21:
        size = True
        print("c")
    if has_spec == False or size == False or has_upper == False:
        return False
    else:
        return True

