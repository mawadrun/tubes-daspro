import fungsi_dasar as fd
import F01 as f1

# Summon Jin                #Note Username belum di test
def summonjin(data_user):
    Validjenis = False
    Validuser = False
    Validpass = False
    if fd.listLen(data_user) < 102:
        print("Jenis jin yang dapat dipanggil:\n (1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n (2) Pembangun - Bertugas membangun candi")
        print('')
        # Pemilihan jenis Jin
        while Validjenis == False:
            jenis = int(input("Masukkan nomor jenis yang ingin dipanggil: "))
            print('')
            if jenis == 1:
                print('Memilih jin "Pengumpul".')
                Validjenis = True
            elif jenis == 2:
                print('Memilih jin "Pembangun".')
                Validjenis = True
            else:
                print(f'Tidak ada jenis jin bernomor “{jenis}”!')

        # Input username
        while Validuser == False:
            username_jin = input("Masukkan username jin: ")
            if cekusername(data_user, username_jin):
                Validuser =  True
            else:
                print(f'Username “{username_jin}” sudah diambil!')
    
        # Input Password
        while Validpass == False:
            password_jin = input('Masukkan password jin: ')
            if len(password_jin) <5 or len(password_jin)> 25:
                print('Password panjangnya harus 5-25 karakter!')
            else:
                print('Mengumpulkan sesajen...\n Menyerahkan sesajen...\n  Membacakan mantra...')
                print(f'Jin {username_jin} berhasil dipanggil!')
                Validpass = True
        return popjin(data_user, username_jin, password_jin, jenis)
    else:
        print(f'Jumlah Jin telah maksimal! (100 jin). {f1.username_()} tidak dapat men-summon lebih dari itu')
        return data_user

## Fungsi pendamping
# Pengecekan Username Jin
def cekusername(data_user, username_jin):
    for i in range(fd.listLen(data_user)):
        if data_user[i][0] == username_jin:       
            return False
    return True

# Masukkan Jin ke list
def popjin(data_user, username_jin, password_jin, jenis):
    tempdata_user = [['' for i in range(3)] for i in range(1+fd.listLen(data_user))]
    lastid = fd.listLen(data_user)
    for i in range(fd.listLen(data_user)):
        for j in range(3):
            tempdata_user[i][j] = data_user[i][j]

    tempdata_user[lastid][0] = str(username_jin)
    tempdata_user[lastid][1] = str(password_jin)
    if jenis == 1:
        tempdata_user[lastid][2] = 'jin_pengumpul'
    else:
        tempdata_user[lastid][2] = 'jin_pembangun'
    return tempdata_user

# cek banyak user
#def banyakuser(data_user):
    #count = 0
    #for i in range(102):
        #if data_user[i][0] != '':
            #count += 1
    #return count