
# ============= FUNGSI STRING ============= #

def strLen(string):
# mengembalikan panjang dari string, tapi ternyata len(string) diperbolehkan
    temp = string + "$" # mark
    i = 0

    while temp[i] != "$":
        i += 1 
    
    return i

def strSplit(string, separator):
# membagi string menjadi list dengan pebagi separator
    newlist = []
    last = 0
    for i in range(strLen(string)):
        if string[i] == separator:
            sect = ""
            for j in range(last, i):
                sect += string[j]
            newlist = appendList(sect, newlist)
            last = i + 1
    sect = ""
    for j in range(last, strLen(string)):
        sect += string[j]
    newlist = appendList(sect, newlist)
    return newlist



# ============= FUNGSI LIST ============= #

def listLen(list):
# mengembalikan panjang dari list
    if list == []:
        return 0
    else:
        temp = list[-1]
        list[-1] = "$" # ganti elemen terakhir dengan mark
        i = 0

        while list[i] != "$":
            i += 1
        
        list[-1] = temp # kemalikan elemen terakhir ke nilai aslinya
        return i + 1
def copyList(list): 
# menyalin list
    newlist = [list[i] for i in range(listLen(list))]
    return newlist

def sliceList(list, imin, imax):
# mengambil sublist dari list (perilaku sama seperti list slicing, list[imin:imax:])
    newlist = ["" for i in range(imax-imin)]
    for i in range(imin, imax):
        newlist[i-imin] = list[i]
    return newlist

def appendList(element, list):
# menaruh element pada ujung list. penggunaan: listBaru = appendList(elemenBaru, listLama)
    newlist = ["" for i in range(listLen(list)+1)]
    for i in range(listLen(list)):
        newlist[i] = list[i]
    newlist[-1] = element
    return newlist

def delList(element, list):
    newlist = ["" for i in range(listLen(list))]
    found = 0
    for i in range(listLen(list)):
        if list[i] != element:
            newlist[i-found] = list[i]
        else:
            found += 1
    return sliceList(newlist, 0, listLen(newlist)-found)

def listSort(list, mode):
# mengurutkan elemen pada list (insertion sort)
    if mode == 'a':
        l = copyList(list)
        for i in range(1, listLen(l)):
            for j in range(i, 0, -1):
                if l[j] < l[j-1]:
                    temp = l[j]
                    l[j] = l[j-1]
                    l[j-1] = temp
        return l
    elif mode == 'd':
        l = copyList(list)
        for i in range(1, listLen(l)):
            for j in range(i, 0, -1):
                if l[j] > l[j-1]:
                    temp = l[j]
                    l[j] = l[j-1]
                    l[j-1] = temp
        return l


# ============= FUNGSI MATRIX ============= #

def matrixSort(matrix, column, mode):
# mengurutkan baris pada matrix berdasarkan nilai column
    if mode == 'a':
        m = copyList(matrix)
        for i in range(1, listLen(m)):
            for j in range(i, 0, -1):
                if m[j][column] < m[j-1][column]:
                    temp = m[j]
                    m[j] = m[j-1]
                    m[j-1] = temp
        return m
    elif mode == 'd':
        m = copyList(matrix)
        for i in range(1, listLen(m)):
            for j in range(i, 0, -1):
                if m[j][column] > m[j-1][column]:
                    temp = m[j]
                    m[j] = m[j-1]
                    m[j-1] = temp
        return m
        

def matrixCount(matrix, column, criteria):
# menghitung jumlah baris yang memenuhi nilai column == criteria
    n = 0
    for i in range(listLen(matrix)):
        if matrix[i][column] == criteria:
            n += 1
    return n

def matrixRank(matrix, column):
# menghitung jumlah kemunculan suatu nilai pada column, lalu mengurutkannya dari yang terbesar
# hasil return matriks dengan elemen list [data, jumlah kemunculan] untuk setiap data
    r = []
    sortedMatrix = matrixSort(matrix, column, 'a')
    lastdata = [sortedMatrix[0][column], 1]
    for i in range(1, listLen(sortedMatrix)):
        if sortedMatrix[i][column] == lastdata[0]:
            lastdata[1] += 1
        else:
            r = appendList(lastdata, r)
            lastdata = [sortedMatrix[i][column], 1]
    r = appendList(lastdata, r)
    return matrixSort(r, 1, 'd')

# NOTE TO SELF: dua fungsi di bawah ini sebaiknya dipindah ke fungsi_terapan.py

def matrixMinLexic(matrix, column):
# mengambil data dengan kemunculan terbanyak pada column
# jika ada lebih dari satu, ambil yang urutan leksikografis terendah
    ranked = matrixRank(matrix, column)
    nTop = 1
    top = ranked[0][1]
    for i in range(1, listLen(ranked)):
        if ranked[i][1] == top:
            nTop += 1
        else:
            top = ranked[i][1]
    return matrixSort(sliceList(ranked, 0, nTop), 0, 'a')[0][0]

def matrixMaxLexic(matrix, column): # MUNGKIN BUGGY, MAGER MERIKSA
# mengambil data dengan kemunculan sedikit pada column
# jika ada lebih dari satu, ambil yang urutan leksikografis tertinggi
    ranked = matrixRank(matrix, column)
    nTop = 1
    top = ranked[listLen(ranked)-1][1]
    for i in range(listLen(ranked)-1, 0, -1):
        if ranked[i][1] == top:
            nTop += 1
        else:
            top = ranked[i][1]
    return matrixSort(sliceList(ranked, 0, nTop), 0, 'd')[0][0]



# Temporary Function (Nantinya bakal diimplementasikan/menggunakan fungsi diatas)
# Fungsi menentukan banyak tipe data dalam 1 baris
def type_(x, seperator):                           
    count = 1
    for i in range(len(x)):
        if x[i] == seperator:
            count+=1
    return count

# Fungsi Memotong baris menjadi array
def split(x, seperator):                           
    i = 0
    split_user = ['' for i in range(type_(x, seperator))]
    for j in range(len(x)):
        if x[j] != seperator:
            split_user[i] += x[j]
        else:
              i += 1 
    return split_user

if __name__ == "__main__": # buat coba2
    loi = [32, 42, 6, 23, 42, 99, 32, 34, 321, 32]
    print(loi)
    k = listSort(loi,'a')
    print(loi)
    print(k)
    print(delList(32, loi))


    
