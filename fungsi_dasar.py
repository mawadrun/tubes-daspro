def strLen(string): # mengembalikan panjang dari string, tapi ternyata len(string) diperbolehkan
    temp = string + "$" # mark
    i = 0

    while temp[i] != "$":
        i += 1 
    
    return i

def listLen(list): # mengembalikan panjang dari list
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

def copyList(list): # menyalin list
    newlist = [list[i] for i in range(listLen(list))]
    return newlist

def appendList(element, list): # menaruh element pada ujung list. penggunaan: listBaru = appendList(elemenBaru, listLama)
    newlist = ["" for i in range(listLen(list)+1)]
    for i in range(listLen(list)):
        newlist[i] = list[i]
    newlist[-1] = element
    return newlist

def strSplit(string, separator): # membagi string menjadi list dengan pebagi separator
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

if __name__ == "__main__": # buat coba2
    list = ["1", "2", "3"]
    string = "tahu bulat di goreng dadakan"
    string2 = "ini\nadalah\nstring\nmultibaris"
    string3 = "ini adalah string kalimat\nyang memiliki\nbanyak baris"

    print(strSplit(string, " "))
    print(strSplit(string2, "\n"))
    string3lines = strSplit(string3, "\n")

    string3final = []
    for i in range(len(string3lines)):
        string3final = appendList(strSplit(string3lines[i], " "), string3final)
    print(string3final)


    
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
