# F12 - Ayam Berkokok

import fungsi_dasar as fd
from F16 import main as exit_

def main(data_user, data_bahan, data_candi):
    jml_candi = fd.listLen(data_candi)
    if jml_candi >= 100:
        print(f"Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi: {jml_candi}\n\nYah, Bandung Bondowoso memenangkan permainan!")
        exit_(data_user, data_bahan, data_candi)
    else:
        print(f"Kukuruyuk.. Kukuruyuk..\n\nJumlah Candi: {jml_candi}\n\nSelamat, Roro Jonggrang memenangkan permainan!\n\n*Bandung Bondowoso angry noise*\nRoro Jonggrang dikutuk menjadi data_candi.")
        exit_(data_user, data_bahan, data_candi)

