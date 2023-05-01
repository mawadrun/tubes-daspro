import fungsi_dasar as fd

# Ubah role jin
def ubahjin(data_user):
    ada = False
    ubahrole_username = input('Masukkan username jin : ')
    for i in range(fd.listLen(data_user)):
        if i != 0 and i != 1:
            if data_user[i][0] == ubahrole_username:
                ada = True
                role_user = fd.strSplit(data_user[i][2], '_')
                opsi = input(f'Jin ini bertipe “{role_user[1]}”. Yakin ingin mengubah ke tipe “{rolelain(role_user[1])}” (Y/N)? ')
                if opsi == 'Y':
                    data_user[i][2] = (f'jin_{rolelain(role_user[1])}')
                elif opsi == 'N':
                    break
        else:
            ada = False
    if ada == False:
        print('Tidak ada jin dengan username tersebut.')
    return(data_user)


# Fungsi role lain
def rolelain(role):
    if role == 'pengumpul':
        return 'pembangun'
    elif role == 'pembangun':
        return 'pengumpul'