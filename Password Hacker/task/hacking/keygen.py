import itertools
# from string import maketrans

i = 0
with open('passwords.txt', 'r') as passwords:
    while i < 4:
        pass_list = []
        pass_seed = passwords.readline().rstrip('\n')
        original = pass_seed
        print(pass_seed)
        pass_seed = pass_seed.translate({ord(i): None for i in '0123456789'})
        trials = list(map(''.join, itertools.product(*zip(pass_seed.upper(), pass_seed.lower()))))
        for trial in trials:
            pass_list.append(original.translate({ord(y): trial[x] for x, y in enumerate(pass_seed)}))
        print(pass_list)
        i += 1
