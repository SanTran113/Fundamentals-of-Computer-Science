# Name: San Tran
# GitHub: SanTran113
# Date: 12 / 04 / 22
import sys
import read

if __name__ == "__main__":
    #puzzle.py images/puzzle.ppm
    img = read.readPPM(sys.argv[1])
    print(sys.argv[1])
    #print(img) y[x
    try:
        # print(f"read image: {read.readPPM(img)}")
        # img = img.readlines(images/, "wb")
        # print(img)
        for h in img:
            # print(h)
            for w in h:
                print(w)
                print(w.red)
                red = w.red * 10
                if red > 255:
                    red = 255
                w.red = red
                w.green = red
                w.blue = red
                # print(w)

        f = open("images/hidden.ppm", "w")
        f.write("P3\n")
        f.write(f"{len(img[0])}, {len(img)}\n")
        f.write("255\n")
        for l in img:
            for l2 in l:
                # for ele in l2:
                f.write(str(l2.red)+"\n")
                f.write(str(l2.green)+"\n")
                f.write(str(l2.blue)+"\n")


    except FileNotFoundError:
        print("No File error")
        sys.exit()
