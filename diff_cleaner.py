#! /bin/python3

diff_file = "diff"

f = open(diff_file)
fo = open("missing_pkg", "w")
L = f.readlines()
f.close()

for line in L:
    if line[0] == '<':
        i = 2
        while line[i] != " ":
            i += 1
        fo.write(line[2:i] + '\n')
        print("Missing package ===> " + line[2::], end="")

print("\nMissing package file is: missing_pkg\n")
fo.close()
