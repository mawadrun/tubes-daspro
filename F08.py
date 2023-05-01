import fungsi_dasar as fd
import F06 as f6
import F07 as f7
import time

def batchkumpul(data_user):
    nPengumpul = fd.matrixCount(data_user, 2, "jin_pengumpul")
    pasir = batu = air = 0
    if nPengumpul > 0:
        print('Mengerahkan {} jin untuk mengumpulkan bahan.'.format(nPengumpul))
        # Loop mengumpulkan bahan dari setiap jin_pengumpul
        for i in range(nPengumpul):
            t = int(time.time())
            getPasir, getBatu, getAir = f7.kumpul(t)
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
    nPembangun = fd.matrixCount(data_user, 2, "jin_pembangun")
    
    # inisalisasi variabel tempdata_jin untuk menampung username jin_pembangun
    tempdata_jin = ['' for i in range(nPembangun)]

    # looping untuk pengisian username jin_pembangun ke tempdata_jin
    i = 0
    while i<nPembangun:
        for j in range(fd.listLen(data_user)):
            if data_user[j][2] == "jin_pembangun":
                tempdata_jin[i] = data_user[j][0]
                i += 1
    
    lenData_Candi = fd.listLen(data_candi)
    if lenData_Candi == 0:
        totalCandi == 0
    else:
        totalCandi = int(data_candi[-1][0])+1

    if nPembangun > 0:
        print('Mengerahkan {} jin untuk membangun candi dengan total bahan {} pasir, {} batu, dan {} air.'.format(nPembangun, data_bahan[0][2], data_bahan[1][2], data_bahan[2][2]))
        tempdata_candi = data_candi
        lastid = fd.listLen(data_candi)
        pasir = batu = air = 0
        # Pengisian candi yang baru dibangun ke tempdata_candi
        j = 0
        for i in range(lastid, nPembangun+fd.listLen(data_candi)):
            t = int(time.time())
            getpasir, getbatu, getair = fd.lcgRandom(t)
            getpasir = (getpasir % 5) + 1
            getbatu = (getbatu % 5) + 1
            getair = (getair % 5) + 1
            pasir += getpasir
            batu += getbatu
            air += getair
            if totalCandi < 100:
                tempdata_candi = fd.appendList([str(i), tempdata_jin[j], getpasir, getbatu, getair], tempdata_candi)
                totalCandi += 1
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