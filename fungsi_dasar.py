
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
    return newlist

def listSort(list):
# mengurutkan elemen pada list (insertion sort)
    l = copyList(list)
    for i in range(1, listLen(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                temp = l[j]
                l[j] = l[j-1]
                l[j-1] = temp
    return l

# ============= FUNGSI MATRIX ============= #

def matrixSort(matrix, column):
# mengurutkan baris pada matrix berdasarkan nilai column
    m = copyList(matrix)
    for i in range(1, listLen(m)):
        for j in range(i, 0, -1):
            if int(m[j][column]) < int(m[j-1][column]):
                temp = m[j]
                m[j] = m[j-1]
                m[j-1] = temp
    return m

def matrixCount(matrix, column, criteria):
# menghitung jumlah baris dengan nilai column == criteria
    n = 0
    for i in range(listLen(matrix)):
        if matrix[i][column] == criteria:
            n += 1
    return n

def matrixRank(matrix, column):
    r = []


# Temporary Function (Nantinya bakal diimplementasikan/menggunakan fungsi diatas)
# Fungsi menentukan banyak tipe data dalam 1 baris
def type_(x):                           
    count = 1
    for i in range(len(x)):
        if x[i] == ';':
            count+=1
    return count

# Fungsi Memotong baris menjadi array
def split(x):                           
    i = 0
    split_user = ['' for i in range(type_(x))]
    for j in range(len(x)):
        if x[j] != ";":
            split_user[i] += x[j]
        else:
              i += 1 
    return split_user

if __name__ == "__main__": # buat coba2
    loi = [32, 42, 6, 23, 42, 99]
    print(loi)
    k = listSort(loi)
    print(loi)


    
