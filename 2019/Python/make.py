import os
import sys

n = 1
try:
    n = int(sys.argv[1])
    if n < 1 or n > 26: raise
except:
    print("Command: python make.py [1 - 25]")
    exit()

os.system(f"mkdir D{n}")
os.system(f"cp template.py D{n}/p1.py")
os.system(f"cp template.py D{n}/p2.py")
