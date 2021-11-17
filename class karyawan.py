class Karyawan:
    '''Dasar kelas untuk semua karyawan'''
    jumlah_karyawan = 0

    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji
        Karyawan.jumlah_karyawan += 1

    def tampilkan_jumlah(self):
        print("Total karyawan:", Karyawan.jumlah_karyawan)

    def tampilkan_profil(self):
        print("Nama :", self.nama)
        print("Gaji :", self.gaji)
        print()

karyawan1 = Karyawan('Eka', 1000000)
karyawan2 = Karyawan('Ocid', 30000000)
karyawan3 = Karyawan('Eve', 30000000)
karyawan4 = Karyawan('avu', 499000)
karyawan5 = Karyawan('ava', 900000)

karyawan3.tampilkan_profil()
print("Total karyawan:", Karyawan.jumlah_karyawan)
