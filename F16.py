import sys 
import F14

def exit(data_user):
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

# menerima input dari pengguna 
while opsi != "y" and opsi != "n" or opsi != "Y" and opsi != "N":
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

# validasi input 
if opsi == "y" or opsi == "Y":
  save(data_user)
  sys.exit()
 elif opsi == "n" or opsi == "N":
  sys.exit()
