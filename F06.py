import fungsi_dasar as fd

def bangun(seed):
    pasir, batu, air = fd.lcgRandom(seed)
    print("Jin menggunakan {} pasir, {} batu, dan {} air.".format(pasir, batu, air))
    return pasir, batu, air