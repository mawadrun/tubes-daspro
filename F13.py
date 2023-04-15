# F13 - Load

import fungsi_dasar as fd

def main(file): # Meng-import file CSV menjadi matrix
    with open(file, 'r') as f:
        lines = f.read()
        lines = fd.strSplit(lines, "\n")
    for i in range(fd.listLen(lines)):
        lines[i] = fd.strSplit(lines[i], ";")
    headellessLines = fd.sliceList(lines, 1, fd.listLen(lines)-1)
    return headellessLines

