# Name: San Tran
# Date: 10 / 24 / 22
# GitHub: SanTran113

import sys

if __name__ == "__main__":
    # l = "Winter, Summer, Spring"
    l = enumerate(sys.argv)
    for element, index in l:
        print(element, index)

# python3 cmdline.py arg1 arg2 arg3

