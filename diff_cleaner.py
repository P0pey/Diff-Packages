#! /bin/python3

diff_file = "diff"

f = open(diff_file)
fo = open("missing_pkg", "w")
L = f.readlines()
f.close()

for line in L:
    if line[0] == '<':
        fo.write(line[2::])
        print("Missing package ===> " + line[2::-1])
fo.close()
