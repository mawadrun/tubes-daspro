import fungsi_dasar as fd

# Membaca file (belum kepakai)
file = open('./csv/user.csv','r')
data_user = file.readlines()

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
                    print(f"Selamat Datang,{username}!")
                    return True
                else:
                    print("Password Salah!")
                    return False
    print("Username tidak terdaftar!")
    return False

## Fungsi meneruskan variabel
# Fungsi username
def username_():
    global username
    return username

# Fungsi menentukan role
def role_():
    global role
    # Kalo password salah role jadi error
    if role[0] == "jin":
        # mendapatkan tipe jin, hilangkan \n
        temprole = fd.split(role[1], '\n')
        return temprole[0]
    else:
        return role[0]