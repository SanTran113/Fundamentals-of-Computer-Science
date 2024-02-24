# Name: San Tran
# GitHub: SanTran113
# Date: 12 / 04 / 22

import sys
import read

if __name__ == "__main__":
    img = read.readPPM(sys.argv[1])
    try:
        count = 0
        # Width
        for h in img:
            count = 0
            for w in h:
                if count + 1 >= len(h):
                    break
                else:
                    red = (h[count][0] + h[count + 1][0]) // 2
                    green = (h[count][1] + h[count + 1][1]) // 2
                    blue = (h[count][2] + h[count + 1][2]) // 2
                    h[count][0] = red
                    h[count][1] = green
                    h[count][2] = blue
                    # print(red)
                    # print(w[0])
                    # print(h[count])
                    count += 2

        # Height
        count = 0
        for h in img:
            for w in h:
                if count + 1 >= len(img[0])//2:
                    break
                else:
                    nextCount = count + len(img[0])
                    red = (h[count][0] + h[count + len(img[0])//2][0]) // 4
                    green = (h[count][1] + h[count + len(img[0])//2][1]) // 4
                    blue = (h[count][2] + h[count + len(img[0])//2][2]) // 4
                    # print(len(img[0])//2)
                    # print(len(h))
                    # print(h[90][0])
                    # print(h)
                    # print(nextCount)
                    # print(len(img[0]))
                    if red > 255:
                        red = 255
                    if green > 255:
                        green = 255
                    if blue > 255:
                        blue = 255
                    h[count][0] = red
                    h[count][1] = green
                    h[count][2] = blue
                    count += 1


        f = open("images/halfed.ppm", "w")
        f.write("P3\n")
        f.write(f"{len(img[0])//2}, {len(img)//2}\n")
        f.write("2 55\n")
        count = 0
        c = 0
        for l in img:
            # print(l)
            if c % 2 == 0:
                for l2 in l:
                    # step = l2[0:len(l2):2]
                    # print(l2)
                    for ele in l2:
                        if count % 2 == 0:
                            f.write(str(ele) + "\n")
                        count += 1
            c += 1

    except FileNotFoundError:
        print("No File error")
        sys.exit()