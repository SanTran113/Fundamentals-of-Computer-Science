from typing import List

from pixel import Pixel

def readPPM(path: str) -> List[List[Pixel]]:
    '''Reads a PPM file as a list of rows of pixels'''
    try:
        f = open(path, 'r')

    except FileNotFoundError:
        print("readPPM could not find the file!")
        return None
    except:
        print("readPPM had an unexpected error!")
        return None
    else:
        f.readline() # Skip "P3" line

        # Read the header information
        width, height, max_color = None, None, None
        while (width == None and height == None):
            header = f.readline()

            # Skip comments
            if header.startswith("#"):
                continue
            # Read Header Data
            else:
                try:
                    fields = header.strip().split()
                    width  = int(fields[0])
                    height = int(fields[1])

                    # Get the maximum value from the next line
                    header = f.readline()
                    header = header.strip()

                    max_color = int(header)
                except:
                    print("readPPM failed to read header")
                    return None

        # Read in the pixel data
        data = []
        for h in range(height):
            row = []
            for w in range(width):
                pixel = None
                try:
                    red = int(f.readline().strip())
                    green = int(f.readline().strip())
                    blue = int(f.readline().strip())
                    pixel = Pixel(red, green, blue)
                except:
                    print("readPPM failed to read pixel data")
                row.append(pixel)
            data.append(row)
        f.close()

        return data
