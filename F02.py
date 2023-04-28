# Fungsi Logout
def logout(status):
    # Status sebagai penanda apakah sudah login atau belum
    if status == True:
        return False
    else:
        print('Logout gagal!\n Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout.')
        return True