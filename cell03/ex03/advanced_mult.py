import sys
if len(sys.argv) != 1:
    print("none")
else:
    table = 0
    while table <= 10:
        i = 0
        result = ""
        while i <= 10:
            result += str(i * table) + " "
            i += 1
        print("Table de", table, ":", result)
        table += 1