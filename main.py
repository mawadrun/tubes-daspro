import fungsi_dasar as fd
import fungsi_terapan as ft

# Program Utama
status = False              # Penanda awal bahwa belum login
def menu():
    global status
    pilihan = input()
    if pilihan == 'login':
        if status == False:
            if ft.login() == True:
                status = True
            else:
                status = False
        else:
            print(f'Login gagal!\n Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.')
        menu()
    elif pilihan == 'logout':
        ft.logout()
        menu()

# Memanggil/Memulai Program
menu()
