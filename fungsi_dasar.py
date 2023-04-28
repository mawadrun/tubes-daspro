import time

# ============= FUNGSI STRING ============= #

def strLen(string):
# mengembalikan panjang dari string, tapi ternyata len(string) diperbolehkan
    temp = string + "$" # mark
    i = 0

    while temp[i] != "$":
        i += 1 
    
    return i

def strInsert(string, char, index):
    newstring = ""
    for i in range(index):
        newstring += string[i]
    newstring += char
    for i in range(index+1, strLen(string)+1):
        newstring += string[i-1]
    return newstring

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

# ============= FUNGSI INTEGER ========== #
def lcgRandom():
    x = int(time.time())
    a = 1664525
    c = 1013904223
    m = 2**32
    tri = [0, 0, 0]

    for i in range(3):
        x = ((a * x) + c) % m
        tri[i] = x
    
    return tri[0], tri[1], tri[2]

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

def joinList(list, separator):
    newstr = ""
    for i in range(listLen(list)-1):
        newstr += str(list[i]) + separator
    newstr += str(list[listLen(list)-1])
    return newstr

def appendList(element, list):
# menaruh element pada ujung list. penggunaan: listBaru = appendList(elemenBaru, listLama)
    newlist = ["" for i in range(listLen(list)+1)]
    for i in range(listLen(list)):
        newlist[i] = list[i]
    newlist[-1] = element
    return newlist


def delList(element, list):
# menghasilkan list baru, yaitu list awal dengan elemen "element" dihapus
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


def matrixRankData(matrix, column, mode):
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

    if mode == 'd':
        return matrixSort(r, 1, 'd')
    elif mode == 'a':
        return matrixSort(r, 1, 'a')
    else:
        return 0
    

def matrixIndexOf(matrix, column, element):
# mengembalikan indeks kemunculan pertama element pada column dari matriks
    for i in range(listLen(matrix)):
        if matrix[i][column] == element:
            return i

 
def matrixColumnSum(matrix, column):
# menghitung jumlah total column dari sebuah matriks
    s = 0
    for i in range(listLen(matrix)):
        s += int(matrix[i][column])
    return s


if __name__ == "__main__": # buat coba2
    print()