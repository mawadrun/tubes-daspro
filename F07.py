import fungsi_dasar as fd
import time

def kumpul(t):
    pasir, batu, air = fd.lcgRandom(t)
    pasir = (pasir % 6)
    batu = (batu % 6)
    air = (air % 6)
    return pasir, batu, air