import time
import fungsi_dasar as fd
import F06 as f6
import F07 as f7

def batchkumpul(data_user):
    # inisaliasi variabel jumlah jin_pengumpul
    nPengumpul = 0
    pasir = batu = air = 0
    # looping untuk menentukan jumlah jin_pengumpul
    for i in range(fd.listLen(data_user)):
        if data_user[i][2] == "jin_pengumpul":
            nPengumpul += 1
    if nPengumpul > 0:
        print('Mengerahkan {} jin untuk mengumpulkan bahan.'.format(nPengumpul))
        # Loop mengumpulkan bahan dari setiap jin_pengumpul
        for i in range(nPengumpul):
            getPasir, getBatu, getAir = f7.kumpul()
            pasir += getPasir
            batu += getBatu
            air += getAir
            # tunda dulu gak sih, nanti timeny tetep barengan (cepet banget executeny :v)
            time.sleep(1)
        print("Jin menemukan total {} pasir, {} batu, dan {} air.".format(pasir, batu, air))
    else:
        print('Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.')
    return pasir, batu, air


def batchbangun(data_user, data_bahan, data_candi):
    # inisialisasi jumlah jin_pembangun
    nPembangun = 0
    # looping untuk menentukan jumlah jin_pembangun
    for i in range(fd.listLen(data_user)):
        if data_user[i][2] == "jin_pembangun":
            nPembangun += 1
    
    # inisalisasi variabel tempdata_jin untuk menampung username jin_pembangun
    tempdata_jin = ['' for i in range(nPembangun)]

    # looping untuk pengisian username jin_pembangun ke tempdata_jin
    i = 0
    while i<nPembangun:
        for j in range(fd.listLen(data_user)):
            if data_user[j][2] == "jin_pembangun":
                tempdata_jin[i] = data_user[j][0]
                i += 1

    if nPembangun > 0:
        print('Mengerahkan {} jin untuk membangun candi dengan total bahan {} pasir, {} batu, dan {} air.'.format(nPembangun, data_bahan[0][2], data_bahan[1][2], data_bahan[2][2]))
        # inisialisasi variabel tempdata_candi untuk menampung data_candi dan data candi yang baru dibangun
        tempdata_candi = [['' for i in range(5)] for i in range(nPembangun+fd.listLen(data_candi))]
        
        lastid = fd.listLen(data_candi)

        # Penyalinan data_candi ke tempadata_candi
        for i in range(lastid):
            for j in range(5):
                tempdata_candi[i][j] = data_candi[i][j]

        # Pengisian candi yang baru dibangun ke tempdata_candi
        j = 0
        for i in range(lastid, fd.listLen(tempdata_candi)):
            pasir, batu, air = fd.lcgRandom()
            tempdata_candi[i][0] = str(i)
            tempdata_candi[i][1] = tempdata_jin[j]
            tempdata_candi[i][2] = pasir
            tempdata_candi[i][3] = batu
            tempdata_candi[i][4] = air
            # tunda dulu gak sih, nanti timeny tetep barengan (cepet banget executeny :v)
            time.sleep(1)
            j += 1


        if (int(data_bahan[0][2]) >= pasir) and (int(data_bahan[1][2]) >= batu) and (int(data_bahan[2][2]) >= air):
            print('Jin berhasil membangun', nPembangun, 'candi.')
            data_bahan[0][2] = str(int(data_bahan[0][2]) - pasir)
            data_bahan[1][2] = str(int(data_bahan[1][2]) - batu)
            data_bahan[2][2] = str(int(data_bahan[2][2]) - air)
            data_candi = tempdata_candi
        else:
            kurangPasir = pasir-int(data_bahan[0][2])
            kurangBatu = batu-int(data_bahan[1][2])
            kurangAir = air-int(data_bahan[2][2])

            if kurangPasir < 0:
                kurangPasir *= -1
            if kurangBatu <0:
                kurangBatu *= -1
            if kurangAir < 0:
                kurangAir *= -1
            print("Bangun gagal. Kurang {} pasir, {} batu, dan {} air.".format(kurangPasir, kurangBatu, kurangAir))
    else:
        print('Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.')
    return data_bahan, data_candi