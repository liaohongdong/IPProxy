import fileinput

with fileinput.input(files="./test.txt") as f:
    for line in f:
        line = line.rstrip()
        num = fileinput.lineno()
        print("#%d\t%s" % (num, line))
