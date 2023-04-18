import fungsi_dasar as fd
import F01 as f1

def bangun(data_bahan, data_candi):
    pasir, batu, air = fd.lcgRandom()
    if (int(data_bahan[0][2]) >= pasir) and (int(data_bahan[1][2]) >= batu) and (int(data_bahan[2][2]) >= air):
        # Kurangi persediaan
        data_bahan[0][2] = str(int(data_bahan[0][2]) - pasir)
        data_bahan[1][2] = str(int(data_bahan[1][2]) - batu)
        data_bahan[2][2] = str(int(data_bahan[2][2]) - air)

        candi = int(data_candi[-1][0]) + 1
        if candi < 100:
            # Inisialisasi list tempdatacandi sepanjang list data_candi ditambah 1 untuk memasukkan candi yang baru dibangun
            tempdata_candi = [['' for i in range(5)] for i in range(1+fd.listLen(data_candi))]
            lastid = fd.listLen(data_candi)
            # Penyalinan list data_candi ke tempdata_candi
            for i in range(lastid):
                for j in range(5):
                    tempdata_candi[i][j] = data_candi[i][j]
            # Pengisian candi yang baru dibangun ke tempdata_candi
            tempdata_candi[lastid][0] = str(lastid)
            tempdata_candi[lastid][1] = str(f1.username_())
            tempdata_candi[lastid][2] = pasir
            tempdata_candi[lastid][3] = batu
            tempdata_candi[lastid][4] = air

            data_candi = tempdata_candi
        print('Candi berhasil dibangun.')
        print("Sisa candi yang perlu dibangun {}".format(100-candi))
    else:
        print('Bahan bangunan tidak mencukupi.')
        print('Candi tidak bisa dibangun!')
    return data_bahan, data_candi