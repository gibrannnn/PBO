class Motor :
    '''dasar kelas untuk semua motor'''
    jumlah_motor = 0
    
    def __init__(self, nama, cc) :
        self.nama = nama
        self.cc = cc
        Motor.jumlah_motor += 1

    def tampilkan_jumlah(self) :
        print("Total motor :", Motor.jumlah_motor)

    def tampilkan_profil(self) : 
        print("Nama :", self.nama)
        print("cc :", self.cc)

#membuat objek pertama dari kelas Motor
motor1 = Motor("vario", 125)
#membuat objek kedua dari kelas Motor
motor2 = Motor("nmax", 155)

motor1.tampilkan_profil()
motor2.tampilkan_profil()
print("Total karyawan :", Motor.jumlah_motor)