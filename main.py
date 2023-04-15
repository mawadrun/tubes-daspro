import fungsi_dasar as fd
import fungsi_terapan as ft

from F09 import main as laporanjin
from F10 import main as laporancandi
from F11 import main as hancurkancandi
from F12 import main as ayamberkokok
from F13 import main as load

# Pembacaan data
data_user = load("./csv/user.csv")
data_candi = load("./csv/candi.csv")
data_bahan = load("./csv/bahan_bangunan.csv")

# Program Utama
status = False              # Penanda awal bahwa belum login
role = ''             
def menu():
    global role
    global status
    print('-----------Login Page-----------')
    print('login atau logout')
    pilihan = input()
    if pilihan == 'login':
        if status == False:
            status = ft.login()
            role = ft.role_()
            print('Masukkan command “help” untuk daftar command yang dapat kamu panggil.')
        else:
            print(f'Login gagal!\n Anda telah login dengan username {ft.username_()}, silahkan lakukan “logout” sebelum melakukan login kembali.')
    elif pilihan == 'logout':
        if status == True:
            status = ft.logout(status)
            role = ''
        elif status == False:
            print('Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout')
    # Memanggil menu bandung
    while role == 'bandung':
        bandungmenu()
    
    
# Menu bila role Bandung (print di fungsi ini hanya untuk pengetesan)
def bandungmenu():
    global role
    global data_user, data_bahan, data_candi
    pilihan = input()
    if pilihan == 'help':
        print('---------Menu Role Bandung---------')
        print('Summon Jin  (summonjin)\nHilangkan Jin  (hapusjin)\nUbah Tipe Jin  (ubahjin)\nAmbil Laporan Jin (laporanjin)\nAmbil Laporan Candi (laporancandi)')
    elif pilihan == 'summonjin':
        data_user = ft.summonjin(data_user)
        print(data_user)
    elif pilihan == 'hapusjin':
        data_user = ft.hapusjin(data_user)
        print(data_user)
    elif pilihan == 'ubahjin':
        data_user = ft.ubahjin(data_user)
        print(data_user)
    elif pilihan == 'laporanjin':
        laporanjin(data_user, data_candi, data_bahan)
    elif pilihan == 'laporancandi':
        laporancandi(data_candi)
    elif pilihan == 'logout':
        role = ''

def roromenu():
    global role
    global data_user, data_bahan, data_candi
    pilihan = input()
    if pilihan == 'hancurkancandi':
        data_candi = hancurkancandi(data_candi)
    elif pilihan == 'ayamberkokok':
        ayamberkokok(data_candi)

# Memanggil/Memulai Program
while True:
    menu()
