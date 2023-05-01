
from F14 import main as save

def main(data_user, data_bahan, data_candi):
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N): ")

  # menerima input dari pengguna 
  while opsi != "y" and opsi != "n" and opsi != "Y" and opsi != "N":
    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N)): ")

  # validasi input 
  if opsi == "y" or opsi == "Y":
    save(data_user, data_bahan, data_candi)
    exit()
  elif opsi == "n" or opsi == "N":
    exit()

