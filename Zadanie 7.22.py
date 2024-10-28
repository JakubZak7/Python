def f(passwd):
    if len(passwd) < 6:
        return False

    if len(passwd) != len(set(passwd)):
        return False
    return True

passwd = "abc123"
result = f(passwd)
print(result)