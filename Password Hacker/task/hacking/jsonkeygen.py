import json
import itertools

keys = list(map(chr, range(97, 123)))
keys.extend(list(map(chr, range(48, 58))))
keys.extend(list(map(chr, range(65, 91))))
print(keys)

incomplete_pass = ''
with open('logins.txt', 'r') as admins:
    i = 0
    while i < 5:
        admin = admins.readline().rstrip('\n')
        credentials = {"login": admin, "password": "12345678"}
        parsed = json.dumps(credentials)
        unparsed = json.loads(parsed)
        print(unparsed['login'])
        incomplete_pass += next(keys)


        i += 1
print(incomplete_pass)