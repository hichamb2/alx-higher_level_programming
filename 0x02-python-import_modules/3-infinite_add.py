#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    res = 0
    for count in range(len(sys.argv) - 1):
        res += int(sys.argv[count + 1])
    print("{}".format(res))
