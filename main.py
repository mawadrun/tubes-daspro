import fungsi_dasar as fd
import fungsi_terapan as ft

# Program Utama
status = False              # Penanda awal bahwa belum login
username = "none"
def menu():
    global status
    global username
    pilihan = input()
    if pilihan == 'login':
        if status == False:
            status = ft.login()
        else:
            print(f'Login gagal!\n Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali.') # Ide: fungsi login() dibuat menjadi return username
    elif pilihan == 'logout':
        ft.logout()

# Memanggil/Memulai Program
while True:
    menu()
