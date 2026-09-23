import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    result = re.findall(sys.argv[1], sys.argv[2])
    if len(result) == 0:
        print("none")
    else:
        print(len(result))