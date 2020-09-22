#! /bin/python3

diff_file = "diff"

f = open(diff_file)
fov = open("missing_version_pkg", "w")
fop = open("missing_pkg", "w")
L = f.readlines()
f.close()

for line in L:
    if line[0] == '<':
        i = 2
        while line[i] != " ":
            i += 1
        fop.write(line[2:i] + '\n')
        fov.write(line[2::])
        print("Version conflict or Missing packages ===> " + line[2::], end="")

fop.close()
fov.close()
