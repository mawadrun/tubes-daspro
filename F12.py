# F12 - Ayam Berkokok

import fungsi_dasar as fd
from F16 import main as exit_

def main(user, bahan, candi):
    jml_candi = fd.listLen(candi)
    if jml_candi >= 100:
        print(f"Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi: {jml_candi}\n\nYah, Bandung Bondowoso memenangkan permainan!")
        exit_(user, bahan, candi)
    else:
        print(f"Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi: {jml_candi}\n\nSelamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi candi.")
        exit_(user, bahan, candi)

