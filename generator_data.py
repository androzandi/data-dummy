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


def createAccount(atype,jml):
    accounttype = atype
    l=[]
    tgl="2"
    for x in range(0,jml):
        if(atype == 3 or atype ==4):
            tgl= randomDate2("1/1/2005", "1/1/2006", random.random())
        dicty= my_dictionary()
        dicty.add("username","")
        dicty.add("password","")
        dicty.add("id_type",atype)
        dicty.add("create_date",tgl)
        dicty.add("update_date",tgl)
        dicty.add("created_by","")
        dicty.add("update_by","")
        l.append(dicty)
    return l        

def createOrangtua(jml):
    l=[]
    l_account = createAccount(2,jml)
    f_name = open("resources/name.txt","r")
    listname = f_name.readlines()
    f_name.close()
    alamat ="J. Bawang"
    tempat = "Bandung"
    kelurahan = "Cicaheum"
    kecamatan = "Kiara Condong"
    kota = "Bandung"
    provinsi = "Jawa Barat"
    agama = "Islam"
    jk = ["L","P"]
    gold = ["A","B","AB","O"]
    i=0
    gelar = ["SD","SMP","SMA","D1","D2","D3","D4","S1","S2","S3"]
    nokk=1232141
    nik =12312
    for name in listname:
        dicty =my_dictionary()
        tgllahir = randomDate2("1/1/1975", "1/1/1980", random.random())
        hp = int(random.random()*10000000 % 10000000)
        username = str(hp)
        l_account[i].update({"username":username})
        l_account[i].update({"password":str(tgllahir)+"a"})
        dicty.add("username",username)
        dicty.add("nama_ayah",name.rstrip('\n'))
        dicty.add("tempat_lahir_ayah",tempat)
        dicty.add("tanggal_lahir_ayah",tgllahir)
        dicty.add("nama_ibu",name.rstrip('\n'))
        dicty.add("tempat_lahir_ibu",tempat)
        dicty.add("tanggal_lahir_ibu",tgllahir)
        dicty.add("alamat_jalan",alamat)
        dicty.add("kelurahan",kelurahan)
        dicty.add("kecamatan",kecamatan)
        dicty.add("kabupaten_kota",kota)
        dicty.add("provinsi",provinsi)
        dicty.add("agama",agama)
        dicty.add("jenis_kelamin",jk[int(random.random()*10 % 2)])
        dicty.add("no_kk",nokk)
        dicty.add("nik",nik)
        dicty.add("gol_darah",gold[int(random.random()*10 % 4)])
        dicty.add("image","--")
        dicty.add("pekerjaan","Wiraswasta")
        dicty.add("penghasilan",1000000)
        dicty.add("pendidikan",gelar[int(random.random()*10%10)])
        l.append(dicty)
        i+=1
        if i==jml:
            break
    createData("account",l_account)
    return l
#jml = jumlah tiap tingkat
def createRombonganBelajar(jml):
    jenjang = 1
    jenis = 1
    # f = open("rombonganbelajar.csv","w+")
    # f.write("idrombel,id_ruangan,nama_rombel\n")
    l= []
    
    for i in range(0,jml*3):
        dicti = my_dictionary()
        idrombel = str(int(jenjang+(i/3)))+str(chr(64+jenis+(i % jml)))
        nama = idrombel
        dicti.add("kode_rombel",idrombel)
        dicti.add("nama_rombel","Kelas "+nama[0]+"-"+nama[1])
        l.append(dicti)
        # f.write(str(idrombel)+","+str(nama)+","+str(ruang +(i%2))+"\n")
    return l

def createSiswa(l_ortu,l_rombel,jml,proba):
    l=[]
    l_account = createAccount(jml)
    f_name = open("resources/name.txt","r")
    list_name = f_name.readlines()
    f_name.close()

    i=0
    for name in list_name:
        dicty = my_dictionary()

def createTU(jml):
    l=[]
    l_account =createAccount(4,jml)
    f_name = open("resources/name.txt","r")
    list_name = f_name.readlines()
    f_name.close()
    i=0
    idadmin="-"
    alamat ="J. Bawang"
    tempat = "Bandung"
    kelurahan = "Cicaheum"
    kecamatan = "Kiara Condong"
    kota = "Bandung"
    provinsi = "Jawa Barat"
    agama = "Islam"
    jk = ["L","P"]
    gold = ["A","B","AB","O"]
    i=0
    status = ["Tetap","Bukan Tetap"]
    gelar = ["D1","D2","D3","D4","S1","S2","S3"]
    nokk=1232141
    nik =12312
    univ = ["Universitas A","Universitas B","Universitas C","Politeknik A","Institut A","Institut C"]
    jurusan = ["T. Informatika","T. Kimia","Pend. Matematika","Matematika","Pend. Olahraga","Akuntansi","T Mesin","T. Elektro"]
    for name in list_name:
        lulusan = str(univ[int(random.random()*10 % 6)]) +":"+ str(jurusan[int(random.random()*10%8)])
        tglcpns = randomDate2("1/1/1995", "1/1/1999", random.random())
        cpns = tglcpns.split("/")
        cpns = "".join(cpns)
        jenis_kelamin = jk[int(random.random()*10 % 2)]
        tgllahir = randomDate2("1/1/1975", "1/1/1980", random.random())
        tgl = randomDate2("1/1/2005", "1/1/2008", random.random())
        if(jenis_kelamin=="L"):
            username = str(tgllahir)+str(cpns)+"1"+makeDigitNumber(3,i)
        else:
            username = str(tgllahir)+str(cpns)+"2"+makeDigitNumber(3,i)
        l_account[i].update({"username":username})
        l_account[i].update({"password":str(tgllahir)+"a"})
        dicty = my_dictionary()
        dicty.add("username",username)
        dicty.add("id_administrasi",idadmin)
        dicty.add("id_status",status[int(random.random()*10%2)])
        dicty.add("nama",name.rstrip('\n'))
        dicty.add("tempat_lahir",tempat)
        dicty.add("tanggal_lahir",tgllahir)
        dicty.add("alamat_jalan",alamat)
        dicty.add("kelurahan",kelurahan)
        dicty.add("kecamatan",kecamatan)
        dicty.add("kabupaten_kota",kota)
        dicty.add("provinsi",provinsi)
        dicty.add("agama",agama)
        dicty.add("jenis_kelamin",jenis_kelamin)
        dicty.add("no_kk",nokk)
        dicty.add("nik",nik)
        dicty.add("gol_darah",gold[int(random.random()*10 % 4)])
        dicty.add("image","--")
        dicty.add("nip",username)
        dicty.add("lulusan",lulusan)
        dicty.add("jenjang_pendidikan",gelar[int(random.random()*10%7)])
        dicty.add("gelar","-")
        dicty.add("create_date",tgl)
        dicty.add("update_date",tgl)
        dicty.add("created_by","")
        dicty.add("update_by","")
        l.append(dicty)
        i+=1
        if i==jml:
            break
    createData("account",l_account)
    return l

def createGuru(jml):
    l=[]
    l_account =createAccount(3,jml)
    f_name = open("resources/name.txt","r")
    list_name = f_name.readlines()
    f_name.close()
    i=0
    iswali="-"
    ispel="-"
    alamat ="J. Bawang"
    tempat = "Bandung"
    kelurahan = "Cicaheum"
    kecamatan = "Kiara Condong"
    kota = "Bandung"
    provinsi = "Jawa Barat"
    agama = "Islam"
    jk = ["L","P"]
    gold = ["A","B","AB","O"]
    i=0
    status = ["Tetap","Bukan Tetap"]
    gelar = ["D1","D2","D3","D4","S1","S2","S3"]
    nokk=1232141
    nik =12312
    univ = ["Universitas A","Universitas B","Universitas C","Politeknik A","Institut A","Institut C"]
    jurusan = ["T. Informatika","T. Kimia","Pend. Matematika","Matematika","Pend. Olahraga","Akuntansi","T Mesin","T. Elektro"]
    for name in list_name:
        lulusan = str(univ[int(random.random()*10 % 6)]) +":"+ str(jurusan[int(random.random()*10%8)])
        tglcpns = randomDate2("1/1/1995", "1/1/1999", random.random())
        cpns = tglcpns.split("/")
        cpns = "".join(cpns)
        jenis_kelamin = jk[int(random.random()*10 % 2)]
        tgllahir = randomDate2("1/1/1975", "1/1/1980", random.random())
        tgl = randomDate2("1/1/2005", "1/1/2008", random.random())
        if(jenis_kelamin=="L"):
            username = str(tgllahir)+str(cpns)+"1"+makeDigitNumber(3,i)
        else:
            username = str(tgllahir)+str(cpns)+"2"+makeDigitNumber(3,i)
        l_account[i].update({"username":username})
        l_account[i].update({"password":str(tgllahir)+"a"})
        dicty = my_dictionary()
        dicty.add("username",username)
        dicty.add("id_status",status[int(random.random()*10%2)])
        dicty.add("nama",name.rstrip('\n'))
        dicty.add("tempat_lahir",tempat)
        dicty.add("tanggal_lahir",tgllahir)
        dicty.add("alamat_jalan",alamat)
        dicty.add("kelurahan",kelurahan)
        dicty.add("kecamatan",kecamatan)
        dicty.add("kabupaten_kota",kota)
        dicty.add("provinsi",provinsi)
        dicty.add("agama",agama)
        dicty.add("jenis_kelamin",jenis_kelamin)
        dicty.add("no_kk",nokk)
        dicty.add("nik",nik)
        dicty.add("gol_darah",gold[int(random.random()*10 % 4)])
        dicty.add("image","--")
        dicty.add("nip",username)
        dicty.add("lulusan",lulusan)
        dicty.add("jenjang_pendidikan",gelar[int(random.random()*10%7)])
        dicty.add("gelar","-")
        dicty.add("is_wali_kelas","-")
        dicty.add("is_wali_pengajar","-")
        dicty.add("create_date",tgl)
        dicty.add("update_date",tgl)
        dicty.add("created_by","")
        dicty.add("update_by","")
        l.append(dicty)
        i+=1
        if i==jml:
            break
    createData("account",l_account)
    return l


def test():
    # mapel=createMapel(2,50)
    # createData("matapelajaran",mapel)
    # account = createAccount(1,100)
    # createData("account",account)
    guru = createGuru(30)
    createData("guru",guru)


def main():
    print("main")

test()

