# F09 - Ambil Laporan Jin

import fungsi_dasar as fd
from F13 import main as load

# NOTE dua fungsi ini mungkin berguna, barangkali saja metode yang sekarang
# digunakan tidak memenuhi kriteria leksiografis soal pada kasus tertentu

# def jinTerajin(matrix, column):
# # mengambil data dengan kemunculan terbanyak pada column
# # jika ada lebih dari satu, ambil yang urutan leksikografis terendah
#     ranked = fd.matrixRankData(matrix, column, 'd')
#     nTop = 1
#     top = ranked[0][1]
#     for i in range(1, fd.listLen(ranked)):
#         if ranked[i][1] == top:
#             nTop += 1
#     return fd.matrixSort(fd.sliceList(ranked, 0, nTop), 0, 'a')[0][0]

# def jinTermalas(matrix, column): # MUNGKIN BUGGY, MAGER MERIKSA
# # mengambil data dengan kemunculan sedikit pada column
# # jika ada lebih dari satu, ambil yang urutan leksikografis tertinggi
#     ranked = fd.matrixRankData(matrix, column, 'a')
#     nTop = 1
#     top = ranked[fd.listLen(ranked)-1][1]
#     for i in range(fd.listLen(ranked)-1, 0, -1):
#         if ranked[i][1] == top:
#             nTop += 1
#         else:
#             top = ranked[i][1]
#     return fd.matrixSort(fd.sliceList(ranked, 0, nTop), 0, 'd')[0][0]
def main(user, candi, bahan):
    jin_pengumpul = fd.matrixCount(user, 2, "jin_pengumpul")
    jin_pembangun = fd.matrixCount(user, 2, "jin_pembangun")

    print(f"Total Jin: {jin_pengumpul + jin_pembangun}")
    print(f"Total Jin Pengumpul: {jin_pengumpul}")
    print(f"Total Jin Pembangun: {jin_pembangun}")
    print(f"Jin Terajin: {fd.matrixRankData(candi, 1, 'd')[0][0]}")
    print(f"Jin Termalas: {fd.matrixRankData(candi, 1, 'd')[-1][0]}")
    print(f"Jumlah Pasir: {bahan[fd.matrixIndexOf(bahan, 0, 'pasir')][2]}")
    print(f"Jumlah Air: {bahan[fd.matrixIndexOf(bahan, 0, 'batu')][2]}")
    print(f"Jumlah Batu: {bahan[fd.matrixIndexOf(bahan, 0, 'air')][2]}")

if __name__ == "__main__":
    user = load("./csv/user.csv")
    candi = load("./csv/candi.csv")
    bahan = load("./csv/bahan_bangunan.csv")

    print(fd.matrixRankData(candi, 1, 'd'))

    main(user, candi, bahan)

