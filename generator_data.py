import random
import time

class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value

#example [makeDigitNumber(3,2)==> 002],[makeDigitNumber(2,1) ==> 001]
def makeDigitNumber(length,angka):
    st = ""
    st = str(angka)
    if length != len(st):
        i=0
        nul = ""
        while i<length-len(st):
            nul += "0"
            i +=1
        st = nul+st
    return st

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))
def randomDate2(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)

#create data to csv
def createData(name,datas):
    f = open("data/"+str(name)+".csv","w+")
    
    # keys = datas[0].keys()
    # print(keys[0])
    pjg = len(datas[0].keys())
    i=0
    j=0
    for data in datas:
        l=[]
        for key in datas[0].keys():
            if i==0:
                if j== pjg-1:
                    f.write(str(key))    
                else:
                    f.write(str(key)+",")
            j+=1
            l.append(data.get(str(key)))
        if i==0:
            f.write("\n")
        writeData(l,f)
        i+=1
    f.close()

def writeData(listdata,f):
    i = 0
    for x in listdata:
        if i == len(listdata)-1:
            f.write(str(x)+"\n") 
        else:
            f.write(str(x)+",")
        i +=1


#jml = jumlah eskul yang dibuat(max 8), pengajar=data pengajar eskul
def createEkstrakurikuler(jml,pengajar):
    f = open("resources/namaeskul.txt","r")
    fs = f.readlines()
    f.close()
    i=0
    hari = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu"]
    jam = ["14:00","15:00","16:00"]
    l=[]
    for eskul in fs:
        kode_eskul = "E"+makeDigitNumber(3,i+1)
        dicti = my_dictionary()
        dicti.add("kode_eskul",kode_eskul)
        dicti.add("id_pengajar",pengajar[i].get("id_pengajar"))
        dicti.add("nama_eskul",eskul.rstrip('\n'))
        dicti.add("hari",hari[int(random.random()*6%6)])
        dicti.add("jam",jam[int(random.random()*3%3)])
        l.append(dicti)
        i+=1
        if i == jml:
            break
    return l

#jml = jumlah matapelajaran yang akan dibuat(max 9),kkm = nilai kkm yang diperlukan(default semua)
def createMapel(jml,kkm):
    f_list_mapel = open("resources/mapel.txt","r")
    list_mapel = f_list_mapel.readlines()
    l=[]
    i = 0
    for mapel in list_mapel:
        for tingkat in range(0,3):
            dicti = my_dictionary()
            kode_mapel = "MP"+ str(tingkat+1)+str(makeDigitNumber(2,i+1))
            dicti.add("kode_mapel",kode_mapel)
            dicti.add("nama_mapel",mapel.rstrip('\n')+" "+str(tingkat+1))
            dicti.add("tingkat",tingkat+1)
            dicti.add("kkm",kkm)
            l.append(dicti)
        i +=1
        if (i==jml):
            break
    f_list_mapel.close()
    return l

def createAccount(atype,max):
    accountype = atype
    username= ""
    katasandi = ""
    alamat ="J. Bawang"
    tempat = "Bandung"
    kelurahan = "Cicaheum"
    kecamatan = "Kiara Condong"
    kota = "Bandung"
    provinsi = "Jawa Barat"
    agama = "Islam"
    jk = ["L","P"]
    gold = ["A","B","AB","O"]
    nokk = 111111111
    nik = 111111112
    if(accountype == 2):
        nokk += 1000
        nik += 1000
    elif(accountype == 3):
        nokk += 100
        nik += 100
    elif(accountype ==4):
        nokk +=10
        nik +=10
    f_name = open("resources/name.txt","r")
    listname = f_name.readlines()
    f_name.close()
    list_account = []
    i = 0
    for name in listname:
        dictionary = my_dictionary()
        if(accountype ==1):
            tgllahir = randomDate2("1/1/1998", "1/1/1999", random.random())
        else:
            tgllahir = randomDate2("1/1/1975", "1/1/1980", random.random())
        katasandi = tgllahir.split("/")
        katasandi = "".join(katasandi)
        nokk +=  10000
        nik += 10000
        dictionary.add("account_type",accountype)
        dictionary.add("kata_sandi",katasandi+"a")
        dictionary.add("nama",name.rstrip('\n'))
        dictionary.add("tempat_lahir",tempat)
        dictionary.add("tanggal_lahir",tgllahir)
        dictionary.add("alamat",alamat)
        dictionary.add("kelurahan",kelurahan)
        dictionary.add("kecamatan",kecamatan)
        dictionary.add("kabupaten_kota",kota)
        dictionary.add("provinsi",provinsi)
        dictionary.add("agama",agama)
        dictionary.add("jenis_kelamin",jk[int(random.random()*10 % 2)])
        dictionary.add("golongan_darah",gold[int(random.random()*10 % 4)])
        dictionary.add("no_kk",nokk)
        dictionary.add("nik",nik)
        list_account.append(dictionary)
        i+=1
        if(i == max):
            break
    
    return list_account

def test():
    # mapel=createMapel(2,50)
    # createData("matapelajaran",mapel)
    account = createAccount(1,100)
    createData("account",account)

def main():
    print("main")

test()