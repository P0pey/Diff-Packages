#! /bin/python3

diff_file = "diff.txt"

f = open(diff_file)
fo = open("missing_packages", "w")
L = f.readlines()
f.close()

for line in L:
    if line[0] == '<':
        fo.write(line[2::])
        print("Missing package ===> " + line[2::])
fo.close()
