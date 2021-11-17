import calendar
print("Selamat datang di ATM Saya")
print("Pilih Option")
print("1. Cek Tanggal Pada Bulan Ini")
option=int(input("Silahkan Pilih Option :"))
if option==1:
    yy = int(input("Masukkan Tahun: "))
    mm = int(input("Masukkan Bulan: "))
    tgl=calendar.month(yy, mm) 
    print("Bulan Ini :",tgl)
else: print ("input anda salah")


