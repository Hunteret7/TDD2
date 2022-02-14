def check_pwd(val):
    if val == "aaaaaaaa":
        return False
    if len(val) < 8:
        return False
    else:
        return True

