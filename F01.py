import fungsi_dasar as fd

# Fungsi Login
def login(data_user):
    global role
    global username                        
    username = input("Username: ")
    password = input("Password: ")
    for i in range(fd.listLen(data_user)):
        if data_user[i][0] == username:
            if data_user[i][1] == password:
                role = fd.strSplit(data_user[i][2],'_')
                print(f"\nSelamat Datang, {username}!")
                return True
            else:
                print("\nPassword Salah!")
                role = ''
                return False
        else:
            role = ''
    print("\nUsername tidak terdaftar!")
    return False

## Fungsi meneruskan variabel
# Fungsi username
def username_():
    global username
    return username

# Fungsi menentukan role
def role_():
    global role
    if role == '':
        return role
    else:
        if role[0] == "jin":
            # mendapatkan tipe jin, hilangkan \n
            temprole = fd.strSplit(role[1], '\n')
            return temprole[0]
        else:
            return role[0]