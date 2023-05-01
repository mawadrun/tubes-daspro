# F09 - Ambil Laporan Jin

import fungsi_dasar as fd

def main(user, candi, bahan):
    jin_pengumpul = fd.matrixCount(user, 2, "jin_pengumpul") # Hitung masing2 tipe jin
    jin_pembangun = fd.matrixCount(user, 2, "jin_pembangun")
    # Print sesuai format
    print(f"Total Jin: {jin_pengumpul + jin_pembangun}")
    print(f"Total Jin Pengumpul: {jin_pengumpul}")
    print(f"Total Jin Pembangun: {jin_pembangun}")
    print(f"Jin Terajin: {fd.matrixRankData(candi, 1, 'd')[0][0]}")
    print(f"Jin Termalas: {fd.matrixRankData(candi, 1, 'd')[-1][0]}")
    print(f"Jumlah Pasir: {bahan[fd.matrixIndexOf(bahan, 0, 'pasir')][2]}")
    print(f"Jumlah Air: {bahan[fd.matrixIndexOf(bahan, 0, 'batu')][2]}")
    print(f"Jumlah Batu: {bahan[fd.matrixIndexOf(bahan, 0, 'air')][2]}")

