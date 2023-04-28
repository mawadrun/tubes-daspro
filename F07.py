import fungsi_dasar as fd

def kumpul():
    pasir, batu, air = fd.lcgRandom()
    pasir = (pasir % 6)
    batu = (batu % 6)
    air = (air % 6)
    return pasir, batu, air