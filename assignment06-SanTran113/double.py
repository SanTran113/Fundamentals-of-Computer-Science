# Name: San Tran
# GitHub: SanTran113
# Date: 12 / 04 / 22

import sys
import read

if __name__ == "__main__":
    img = read.readPPM(sys.argv[1])
    try:
        f = open("images/doubled.ppm", "w")
        f.write("P3\n")
        f.write(f"{2 * len(img[0])}, {2 * len(img)}\n")
        f.write("255\n")

        #[[[20, 20, 20], [120, 30, 50], [40, 70, 80]]]
        for l in img:
            for l2 in l:
                for ele in l2:
                    f.write(str(ele) + "\n")
                for ele in l2:
                    f.write(str(ele) + "\n")
            for l2 in l:
                for ele in l2:
                    f.write(str(ele) + "\n")
                for ele in l2:
                    f.write(str(ele) + "\n")

    except FileNotFoundError:
        print("No File error")
        sys.exit()