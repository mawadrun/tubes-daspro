import fungsi_dasar as fd


def save(matrix, file): # Meng-export matrix ke file (overwrite)
    newmatrix = fd.copyList(matrix)
    # baca judul kolom
    with open(file, 'r') as f:
        title = f.readline()
    # tulis data
    with open(file, 'w') as f:
        f.writelines(title) # tulis judul kolom
        for i in range(fd.listLen(newmatrix)):
            newmatrix[i] = fd.joinList(newmatrix[i], ";")
            if i == fd.listLen(newmatrix) - 1:
                f.writelines(newmatrix[i])
            else:
                f.writelines(newmatrix[i] + "\n")
        f.writelines("\n")

def main(user, bahan, candi):
    save(user, "./csv/user.csv")
    save(bahan, "./csv/bahan_bangunan.csv")
    save(candi, "./csv/candi.csv")

