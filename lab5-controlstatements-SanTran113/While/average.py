# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113


if __name__ == "__main__": # This is to enable a "play" button in PyCharm
    # You will calculate the average of this list
    values = [3.33, 45.0, 12.5, 80.0, 45.0, 16.0]

    # Write your code here
    index = 0
    total = 0
    while index < len(values):
        print(values[index])
        total = total + values[index]
        index += 1
    output = total / len(values)
    print(output)
