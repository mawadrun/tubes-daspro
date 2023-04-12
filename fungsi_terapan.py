import fungsi_dasar as fd

# Membaca file (belum kepakai)
file = open('./csv/user.csv','r')
data_user = file.readlines()

## Fungsi Utama
# Fungsi Login
def login():
    global role
    global username                        
    username = input("Username: ")
    password = input("Password: ")
    for line in data_user:
        #Agar Baris pertama dalam file tidak di baca
        if line != data_user[0]:       
            user = fd.split(line, ';')
            if user[0] == username:
                if user[1] == password:
                    role = fd.split(user[2],'_')
                    print(f"Selamat Datang,{username} !")
                    return True
                else:
                    print("Password Salah!")
                    return False
    print("Username tidak terdaftar!")
    return False

# Fungsi Logout
def logout(status):
    # Status sebagai penanda apakah sudah login atau belum
    if status == True:
        return False
    else:
        print('Logout gagal!\n Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.')

# Summon Jin
def summonjin(data_user):
    global username
    Validjenis = False
    Validuser = False
    Validpass = False
    if banyakuser(data_user) < 102:
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
        print(f'Jumlah Jin telah maksimal! (100 jin). {username} tidak dapat men-summon lebih dari itu')
        return data_user

# Fungsi hapus jin
def hapusjin(data_user):
    ada = False
    hapus_username = input("Masukkan username jin: ")
    for i in range(102):
        if data_user[i][0] == hapus_username:
            ada = True
            opsi = input(f'Apakah anda yakin ingin menghapus jin dengan username {hapus_username} (Y/N)? ')
            if opsi == 'Y':
                data_user[i][0] = ''
                data_user[i][1] = ''
                data_user[i][2] = ''
            elif opsi == 'N':
                break
    if ada == False:
        print('Tidak ada jin dengan username tersebut.')
    return(data_user)

# Ubah role jin
def ubahjin(data_user):
    ada = False
    ubahrole_username = input('Masukkan username jin : ')
    for i in range(102):
        if data_user[i][0] == ubahrole_username:
            ada = True
            role_user = fd.split(data_user[i][2], '_')
            opsi = input(f'Jin ini bertipe “{role_user[1]}”. Yakin ingin mengubah ke tipe “{rolelain(role_user[1])}” (Y/N)? ')
            if opsi == 'Y':
                data_user[i][2] = (f'jin_{rolelain(role_user[1])}')
            elif opsi == 'N':
                break
    if ada == False:
        print('Tidak ada jin dengan username tersebut.')
    return(data_user)

## Fungsi pendamping
# Pengecekan Username Jin
def cekusername(data_user, username_jin):
    for i in range(102):
        if data_user[i][0] == username_jin:       
            return False
    return True

# Masukkan Jin ke list
def popjin(data_user, username_jin, password_jin, jenis):
    for i in range(102):
        if data_user[i][0] == '':
            data_user[i][0] = str(username_jin)
            data_user[i][1] = str(password_jin)
            if jenis == 1:
                data_user[i][2] = 'jin_pengumpul'
            else:
                data_user[i][2] = 'jin_pembangun'
            break
    return data_user

# cek banyak user
def banyakuser(data_user):
    count = 0
    for i in range(102):
        if data_user[i][0] != '':
            count += 1
    return count

# Fungsi role lain
def rolelain(role):
    if role == 'pengumpul':
        return 'pembangun'
    elif role == 'pembangun':
        return 'pengumpul'

## Fungsi meneruskan variabel
# Fungsi username
def username_():
    global username
    return username

# Fungsi menentukan role
def role_():
    global role
    return role[0]