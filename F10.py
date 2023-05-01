# F10 - Ambil Laporan Candi

import fungsi_dasar as fd
# from F13 import main as load

def candiTer(apa, data_candi):
# menentukan data_candi ter(mahal/murah) dalam format [id data_candi, harga]
    pricelist = []
    for i in range(fd.listLen(data_candi)):
        id_candi = data_candi[i][0]
        price_candi = (int(data_candi[i][2])*10000 + int(data_candi[i][3])*15000 + int(data_candi[i][4])*7500)
        pricelist = fd.appendList([id_candi, price_candi], pricelist)
    pricelist = fd.matrixSort(pricelist, 1, 'd')
    if apa == 'mahal': # Paling atas = termahal
        return pricelist[0]
    elif apa == 'murah': # Paling bawah = termurah
        return pricelist[fd.listLen(pricelist)-1]
    
def kasihtitik(x): # Ubah 1000000 menjadi 1.000.000 (contoh)
    ns = str(x)
    for i in range(fd.strLen(ns), 3, -3):
        ns = fd.strInsert(ns, '.', i-3)
    return ns



def main(data_candi): # Print sesuai format, gunakan fungsi yang diimplementasi di atas
    print(f"Total Candi: {fd.listLen(data_candi)}")
    print(f"Total Pasir yang digunakan: {fd.matrixColumnSum(data_candi, 2)}")
    print(f"Total Batu yang digunakan: {fd.matrixColumnSum(data_candi, 3)}")    
    print(f"Total Air yang digunakan: {fd.matrixColumnSum(data_candi, 4)}")
    print(f"ID Candi Termahal: {candiTer('mahal', data_candi)[0]} (Rp {candiTer('mahal', data_candi)[1]})")
    print(f"ID Candi Termurah: {candiTer('murah', data_candi)[0]} (Rp {candiTer('murah', data_candi)[1]})")

