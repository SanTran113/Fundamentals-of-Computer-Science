# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
    value_1 = 0
    value_2 = 0
    while value_1 >= value_2:
        print("Performing an iteration of the loop:")
        print(f"Currently, value_1 = {value_1} and value_2 = {value_2}")
        value_1 += 1
        value_2 += 1
        # Add code here
        if value_1 == 10:
            value_1 = 5
            print(value_1 >= value_2)


