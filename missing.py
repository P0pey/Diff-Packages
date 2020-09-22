#! /bin/python3

f = open("diff2")
L = f.readlines()
f.close()

fo = open("missing_pkg", "w")

for line in L:
    if line[0] == '<':
        fo.write(line[2::])
        print("Missing Package ===> " + line[2::], end="")

print("\nList of missing package: missing_pkg\n")
fo.close()
