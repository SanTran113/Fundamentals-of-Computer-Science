# Name: San Tran
# GitHub: SanTran113
# Date: 12 / 04 / 22

import sys
import read
from read import readPPM

if __name__ == "__main__":
    img = read.readPPM(sys.argv[1])
    try:
        for h in img:
            for w in h:
                red = w[0] * 0.393 + w[1] * 0.769 + w[2] * 0.189
                green = w[0] * 0.349 + w[1] * 0.686 + w[2] * 0.168
                blue = w[0] * 0.272 + w[1] * 0.534 + w[2] * 0.131
                if red > 255:
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255
                w[0] = int(red)
                w[1] = int(green)
                w[2] = int(blue)
                print(w)

        f = open("images/sepia.ppm", "w")
        f.write("P3\n")
        f.write(f"{len(img[0])}, {len(img)}\n")
        f.write("255\n")
        for l in img:
            for l2 in l:
                for ele in l2:
                    f.write(str(ele)+"\n")
    except FileNotFoundError:
        print("No File error")
        sys.exit()