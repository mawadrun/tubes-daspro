import fungsi_dasar as fd

# Fungsi hapus jin
def hapusjin(data_user):
    ada = False
    lewat = False
    hapus_username = input("Masukkan username jin: ")
    tempdata_user = [['' for i in range(3)] for i in range(fd.listLen(data_user)-1)]
    for i in range(fd.listLen(data_user)):
        if data_user[i][0] == hapus_username:
            id = i
            ada = True
    for i in range(fd.listLen(data_user)-1):
        if i == id:
            lewat = True
        if lewat == False:
            for j in range(3):
                tempdata_user[i][j] = data_user[i][j]
        elif lewat == True:
            for j in range(3):
                tempdata_user[i][j] = data_user[i+1][j]
    if ada == False:
        print('Tidak ada jin dengan username tersebut.')
        return data_user
    elif ada == True:
        return tempdata_user