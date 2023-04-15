# F10 - Ambil Laporan Candi

import fungsi_dasar as fd
from F13 import main as load

def candiTer(apa, candi):
# menentukan candi ter(mahal/murah) dalam format [id candi, harga]
    pricelist = []
    for i in range(fd.listLen(candi)):
        id_candi = candi[i][0]
        price_candi = (int(candi[i][2])*10000 + int(candi[i][3])*15000 + int(candi[i][4])*7500)
        pricelist = fd.appendList([id_candi, price_candi], pricelist)
    pricelist = fd.matrixSort(pricelist, 1, 'd')
    if apa == 'mahal':
        return pricelist[0]
    elif apa == 'murah':
        return pricelist[fd.listLen(pricelist)-1]
    
def kasihtitik(x):
    ns = str(x)
    for i in range(fd.strLen(ns), 3, -3):
        ns = fd.strInsert(ns, '.', i-3)
    return ns



def main(candi):
    print(f"Total Candi: {fd.listLen(candi)}")
    print(f"Total Pasir yang digunakan: {fd.matrixColumnSum(candi, 2)}")
    print(f"Total Batu yang digunakan: {fd.matrixColumnSum(candi, 3)}")    
    print(f"Total Air yang digunakan: {fd.matrixColumnSum(candi, 4)}")
    print(f"ID Candi Termahal: {candiTer('mahal', candi)[0]} (Rp {candiTer('mahal', candi)[1]})")
    print(f"ID Candi Termurah: {candiTer('murah', candi)[0]} (Rp {candiTer('murah', candi)[1]})")

if __name__ == '__main__':
    user = load("./csv/user.csv")
    candi = load("./csv/candi.csv")
    bahan = load("./csv/bahan_bangunan.csv")

    main(candi)
