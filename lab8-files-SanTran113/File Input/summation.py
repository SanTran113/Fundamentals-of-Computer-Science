# Name: San Tran
# Date: 11 / 9 / 22
# GitHub: SanTran113
from typing import Optional


def summation() -> Optional[float]:
    print('Enter your inputFile name:')
    inputFile = input()
    try:
        f = open(inputFile, "r")
        lines = f.readlines()
        for line in lines:
            try:
                x = line.split(" ")
                print(x)
                sum = float(x[0]) + float(x[1])
                print(sum)
            except ValueError:
                print("error")
            except IndexError:
                print("error")
    except FileNotFoundError:
        print("NoFile")


if __name__ == "__main__":
    summation()