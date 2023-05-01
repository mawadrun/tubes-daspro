import fungsi_dasar as fd

def main(file): # Meng-import file CSV menjadi matrix
    with open(file, 'r') as f:
        lines = f.read()
        lines = fd.strSplit(lines, "\n") # Bagi per baris
    for i in range(fd.listLen(lines)):
        lines[i] = fd.strSplit(lines[i], ";") # Bagi per kolom
    headellessLines = fd.sliceList(lines, 1, fd.listLen(lines)-1)
    return headellessLines

