import fungsi_dasar as fd
import F01 as f1
import time

def bangun(data_bahan, data_candi):
    t = int(time.time())
    pasir, batu, air = fd.lcgRandom(t)
    pasir = (pasir % 5) + 1
    batu = (batu % 5) + 1
    air = (air % 5) + 1
    if (int(data_bahan[0][2]) >= pasir) and (int(data_bahan[1][2]) >= batu) and (int(data_bahan[2][2]) >= air):
        # Kurangi persediaan
        data_bahan[0][2] = str(int(data_bahan[0][2]) - pasir)
        data_bahan[1][2] = str(int(data_bahan[1][2]) - batu)
        data_bahan[2][2] = str(int(data_bahan[2][2]) - air)

        lenData_Candi = fd.listLen(data_candi)
        if lenData_Candi == 0:
            totalCandi == 0
        else:
            totalCandi = int(data_candi[-1][0])+1

        if totalCandi < 100:
            totalCandi += 1
            # Inisialisasi list tempdatacandi sepanjang list data_candi ditambah 1 untuk memasukkan candi yang baru dibangun
            lastid = fd.listLen(data_candi)
            data_candi = fd.appendList([str(lastid), str(f1.username_()), pasir, batu, air], data_candi)

        print('Candi berhasil dibangun.')
        print("Sisa candi yang perlu dibangun {}".format(100-totalCandi))
    else:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')
    return data_bahan, data_candi