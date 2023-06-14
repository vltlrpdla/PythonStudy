han = open('exfile.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()

    # guardian in a compound statement
    # shortest circuit evaluation, this 'OR' statement check first condition and if that is true, ignore second condition(not executing that)
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])