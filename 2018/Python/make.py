import os

#
# This script creates 25 directories in the current directory
# named d1 to d25. Each directory contains two files which are
# both copies of template.py with N replaced with the current
# day number
#

t = open("template.py").read()

for d in range(1, 25 + 1):
    name = "d" + str(d)
    os.system("mkdir " + name)

    f = open(name + "/" + "p1.py", 'w')
    program_text = t.replace("N", name[1:])
    f.write(program_text)

    f = open(name + "/" + "p2.py", 'w')
    program_text = t.replace("N", name[1:])
    f.write(program_text)
