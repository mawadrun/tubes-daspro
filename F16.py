
import F14

def exit():
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

# menerima input dari pengguna 
while opsi != "y" and opsi != "n" or opsi != "Y" and opsi != "N":
  opsi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")

# validasi input 
if opsi == "y" or opsi == "Y":
  F14.save()
  sys.exit()
 elif opsi == "n" or opsi == "N":
  sys.exit()

