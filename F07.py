import fungsi_dasar as fd

def kumpul(seed):
    pasir, batu, air = fd.lcgRandom(seed)
    print("Jin menemukan {} pasir, {} batu, dan {} air.".format(pasir, batu, air))
    return pasir, batu, air