def missing_char(str, n):
    removed = str.replace(str[n], "")
    return removed
print(missing_char("kanat",2))