fh = open('exfile.txt')
#print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper()) 