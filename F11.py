# F11 - Hancurkan Candi

import fungsi_dasar as fd

def main(data_candi):
    id_candi = input("Masukkan ID Candi: ")
    if fd.matrixIndexOf(data_candi, 0, str(id_candi)) == None:
        print("\nTidak ada data_candi dengan ID tersebut")
        return data_candi
    
    index_candi = fd.matrixIndexOf(data_candi, 0, str(id_candi)) # Ambil index matrix data_candi berdasarkan ID

    confirm = str(input(f"Apakah anda yakin ingin menghancurkan candi ID : {id_candi} (Y/N)? "))
    while (confirm != "Y") and (confirm != "N"): # Ulangi terus jika tidak valid
        print("Input tidak valid.")
        confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID : {id_candi} (Y/N)? ")
    # Jika input valid
    if confirm == "Y" or confirm == "y":
        data_candi = fd.delList(data_candi[index_candi], data_candi)
        print("\nCandi telah berhasil dihancurkan.")
        return data_candi
    elif confirm == "N" or confirm == "n":
        print("\nProses dibatalkan.")

