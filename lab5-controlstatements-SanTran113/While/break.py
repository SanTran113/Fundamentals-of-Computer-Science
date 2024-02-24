# Name: San Tran
# Date: 10 / 21 / 22
# Github: SanTran113

if __name__ == "__main__": # This is to enable a "play" button in PyCharm
    value = 0
    while True:
        # Add code here
        print(value)
        # Do not modify this code
        value += 1
        print("Stuck in an endless loop...")
        if (value == 8):
            break
    # This should output a value of 8
    print(f"Ended with value = {value}")
