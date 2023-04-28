# F11 - Hancurkan Candi

import fungsi_dasar as fd
from F13 import main as load

def main(candi):
    id_candi = input("Masukkan ID Candi: ")
    if fd.matrixIndexOf(candi, 0, str(id_candi)) == None:
        print("\nTidak ada candi dengan ID tersebut")
        return candi
    
    index_candi = fd.matrixIndexOf(candi, 0, str(id_candi))

    confirm = str(input(f"Apakah anda yakin ingin menghancurkan candi ID : {id_candi} (Y/N)? "))
    while (confirm != "Y") and (confirm != "N"):
        print("Input tidak valid.")
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID : {id_candi} (Y/N)? ")
        
    if confirm == "Y" or confirm == "y":
        candi = fd.delList(candi[index_candi], candi)
        print("\nCandi telah berhasil dihancurkan.")
        return candi
    elif confirm == "N" or confirm == "n":
        print("\nProses dibatalkan.")

if __name__ == '__main__':
    candi = load("./csv/candi.csv")
    print(candi)
    candi = main(candi)
    print(candi)
