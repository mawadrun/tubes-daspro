
from F14 import main as save

def main(user, bahan, candi):
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

  # menerima input dari pengguna 
  while opsi != "y" and opsi != "n" and opsi != "Y" and opsi != "N":
    opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

  # validasi input 
  if opsi == "y" or opsi == "Y":
    save(user, bahan, candi)
    exit()
  elif opsi == "n" or opsi == "N":
    exit()

