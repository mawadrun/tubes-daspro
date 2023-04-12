import fungsi_dasar as fd

# Fungsi Login
def login():
    global username                        
    file = open('./csv/user.csv','r')
    baris_user = file.readlines()
    username = input("Username: ")
    password = input("Password: ")
    for line in baris_user:
        #Agar Baris pertama dalam file tidak di baca
        if line != baris_user[0]:       
            user = fd.split(line, ';')
            if user[0] == username:
                if user[1] == password:
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

# Fungsi username
def username_():
    global username
    return username
