keys = list(map(chr, range(97, 123)))
keys.extend(list(map(chr, range(48, 58))))

print(len(keys))
print(keys[35])


def recursive_keys(i, keytry):
    if i // 36 <= 1:
        keytry.append(i % 36)
        print(keytry)
        return keytry
    elif i // 36 < 36:
        keytry.append(i // 36)
        print(keytry)
        recursive_keys(i % 36, keytry)
    else:


i = 1582

print(recursive_keys(i, keytry=[]))
# todo itertools combinations, depending on how many times number can be divided by 36
