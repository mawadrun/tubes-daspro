import fungsi_dasar as fd
import os


def save(matrix, file): # Meng-export matrix ke file (overwrite)
  newmatrix = fd.copyList(matrix)
  # baca judul kolom
  with open(file, 'r') as f:
      title = f.readline()
  # tulis data
  with open(file, 'w') as f:
      f.writelines(title) # tulis judul kolom
      for i in range(fd.listLen(newmatrix)):
          newmatrix[i] = fd.joinList(newmatrix[i], ";") # Gabungkan kolom dengan ; menjadi satu baris
          if i == fd.listLen(newmatrix) - 1:
              f.writelines(newmatrix[i])
          else:
              f.writelines(newmatrix[i] + "\n") # Gabungkan setiap baris menjadi sebuah string
      f.writelines("\n") # Tulis ke csv

def main(user, bahan, candi):
  folder = str(input("Masukkan nama folder: "))

  if folder == "None":
    print("Tidak ada nama folder yang diberikan!")
  else:
    if os.path.isdir(f"./save/{folder}") == False: # cek directory ada / tidak
      print("Saving...")
      print(f"Membuat folder {folder}...")
      # Buat direktori & file jika tidak ditemukan
      os.makedirs(f"./save/{folder}")
      p = open("./save/" + folder + "/user.csv", 'w+')
      p.writelines("username;password;role\n")
      q = open("./save/" + folder + "/bahan_bangunan.csv", 'w+')
      q.writelines("nama;deskripsi;jumlah\n")
      r = open("./save/" + folder + "/candi.csv", 'w+')
      r.writelines("id;pembuat;pasir;batu;air\n")
      p.close()
      q.close()
      r.close()
    else:
      print("Saving...")
    # Simpan hasil permainan
    save(user, "./save/" + folder + "/user.csv")
    save(bahan, "./save/" + folder + "/bahan_bangunan.csv")
    save(candi, "./save/" + folder + "/candi.csv")
    print(f"Berhasil menyimpan data di folder {folder}!")


