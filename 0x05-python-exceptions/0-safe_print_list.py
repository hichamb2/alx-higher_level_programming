#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    j = 0
    try:
        for i in my_list:
            if j < x:
                print(f"{i}", end="")
                j += 1
            else:
                break
        print()
        return (j)
    except (IndexError, TypeError):
        print("")
