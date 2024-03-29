import time
import argparse 
import os
import fungsi_dasar as fd

import F01 as f1
import F02 as f2
import F03 as f3
import F04 as f4
import F05 as f5
import F06 as f6
import F07 as f7
import F08 as f8
from F09 import main as laporanjin
from F10 import main as laporancandi
from F11 import main as hancurkancandi
from F12 import main as ayamberkokok
from F13 import main as load
from F14 import main as save
from F15 import main as help_
from F16 import main as exit_



## JIKA INGIN MENAMBAHKAN OPSI LOGOUT PADA MENU SESUAI ROLE COPY CODE INI
# elif pilihan == 'logout':
#     role = ''
#     status = f2.logout(status)





# Program Utama
status = False              # Penanda awal bahwa belum login
role = ''             

def menu():
    global role
    global status
    global data_user
    global folder
    
    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
    pilihan = input('>>> ')
    if pilihan == 'help':
        help_(role)
    elif pilihan == 'login':
        if status == False:
            status = f1.login(data_user)
            role = f1.role_()
        else:
            print(f'Login gagal!\n Anda telah login dengan username {f1.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')
    elif pilihan == 'logout':
        status = f2.logout(status)
        role = ''
    elif pilihan == 'save':
        save(data_user, data_bahan, data_candi)
    elif pilihan == 'exit':
        exit_(data_user, data_bahan, data_candi)
    
    # Memanggil menu bandung
    while role == 'bandung':
        bandungmenu()

    while role == 'roro':
        roromenu()
    # Memanggil menu jin pengumpul
    while role == 'pengumpul':
        pengumpulMenu()
    while role == 'pembangun':
        pembangunMenu()
    
    
# Menu bila role Bandung (print di fungsi ini hanya untuk pengetesan)
def bandungmenu():
    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
    global status
    global role
    global data_user, data_bahan, data_candi
    pilihan = input('>>> ')
    if pilihan == 'help':
        help_(role)

    # Role-specific commands
    elif pilihan == 'summonjin':
        data_user = f3.summonjin(data_user)
    if pilihan == 'hapusjin':
        data_user = f4.hapusjin(data_user)
    if pilihan == 'ubahjin':
        data_user = f5.ubahjin(data_user)
    if pilihan == "batchkumpul":
        pasir, batu, air = f8.batchkumpul(data_user)
        data_bahan[0][2] = str(int(data_bahan[0][2]) + pasir)
        data_bahan[1][2] = str(int(data_bahan[1][2]) + batu)
        data_bahan[2][2] = str(int(data_bahan[2][2]) + air)
    if pilihan == "batchbangun":
        data_bahan, data_candi = f8.batchbangun(data_user, data_bahan, data_candi)
    if pilihan == 'laporanjin':
        laporanjin(data_user, data_candi, data_bahan)
    if pilihan == 'laporancandi':
        laporancandi(data_candi)
    if pilihan == 'logout':
        role = ''
        status = f2.logout(status)
    if pilihan == 'login':
        print(f'Login gagal!\n Anda telah login dengan username {f1.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')
    
    # Game commands
    if pilihan == 'save':
        save(data_user, data_bahan, data_candi)
    if pilihan == 'exit':
        exit_(data_user, data_bahan, data_candi)


def roromenu():
    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
    global status
    global role
    global data_user, data_bahan, data_candi
    pilihan = input(">>> ")
    if pilihan == 'help':
        help_(role)

    # Role-specific commands
    if pilihan == 'hancurkancandi':
        data_candi = hancurkancandi(data_candi)
    if pilihan == 'ayamberkokok':
        ayamberkokok(data_user, data_bahan, data_candi)
    if pilihan == 'logout':
        role = ''
        status = f2.logout(status)

    # Account commands
    if pilihan == 'login':
        print(f'Login gagal!\n Anda telah login dengan username {f1.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')

    # Game commands
    if pilihan == 'save':
        save(data_user, data_bahan, data_candi)
    if pilihan == 'exit':
        exit_(data_user, data_bahan, data_candi)

# Menu akses jin
def pengumpulMenu():
    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
    global status
    global role
    global data_user, data_bahan, data_candi
    pilihan = input(">>> ")
    if pilihan == 'help':
        help_(role)

    # Role-specific commands
    if pilihan == "kumpul":
        t = int(time.time())
        pasir, batu, air = f7.kumpul(t)
        print("Jin menemukan {} pasir, {} batu, dan {} air.".format(pasir, batu, air))
        # Tambahkan ke persediaan
        data_bahan[0][2] = str(int(data_bahan[0][2]) + pasir)
        data_bahan[1][2] = str(int(data_bahan[1][2]) + batu)
        data_bahan[2][2] = str(int(data_bahan[2][2]) + air)

    # Account commands
    if pilihan == 'logout':
        role = ''
        status = f2.logout(status)
    if pilihan == 'login':
        print(f'Login gagal!\n Anda telah login dengan username {f1.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')

    # Game commands
    if pilihan == 'save':
        save(data_user, data_bahan, data_candi)
    if pilihan == 'exit':
        exit_(data_user, data_bahan, data_candi)


def pembangunMenu():
    print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
    global status
    global role
    global data_user, data_bahan, data_candi
    pilihan = input(">>> ")
    if pilihan == 'help':
        help_(role)

    # Role-specific commands
    if pilihan == "bangun":
        data_bahan, data_candi = f6.bangun(data_bahan, data_candi)
    
    # Account commands
    if pilihan == 'logout':
        role = ''
        status = f2.logout(status)
    if pilihan == 'login':
        print(f'Login gagal!\n Anda telah login dengan username {f1.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')

        # Game commands
    if pilihan == 'save':
        save(data_user, data_bahan, data_candi)
    if pilihan == 'exit':
        exit_(data_user, data_bahan, data_candi)



# Pembacaan data default
# data_user = load("./new/user.csv")
# data_bahan = load("./new/bahan_bangunan.csv")
# data_candi = load("./new/candi.csv")

# Pembacaan data menggunakan parser
parser = argparse.ArgumentParser()
parser.add_argument("load", help="Masukan nama folder yang ingin di load!",nargs='?')
args = parser.parse_args()
folder = str(args.load)
if folder == "None":
    print("Tidak ada nama folder yang diberikan!")
elif os.path.isdir(folder) == False: #cek directory ada / tidak
    print(f"Folder \"{folder}\" tidak ditemukan.")
else:
    print("Memuat file...")
    data_user = load("./" + str(folder) + "/user.csv")
    data_candi = load("./" + str(folder) + "/candi.csv")
    data_bahan = load("./" + str(folder) + "/bahan_bangunan.csv")
    print("File berhasil dimuat!")

    # Memanggil/Memulai Program
    print("                               /                              ")
    print("                  =           ==           =                  ")
    print("                 = =         =  =         = =                 ")
    print("                =   =       =    =       =   =                ")
    print("               =     =     =      =     =     =               ")
    print("              =========   ==========   =========              ")
    print("              = = = = =   = = == = =   = = = = =              ")
    print("             =========== ============ ===========             ")
    print("             =  = = =  = =  = == =  = =  = = =  =             ")
    print("             =========== ============ ===========             ")
    print("               =       Bandung Bondowoso,    =                ")
    print("              ===       Roro Jonggrang,     ===               ")
    print("               =      dan Candi Prambanan    =                 \n")
    while True:
        menu()