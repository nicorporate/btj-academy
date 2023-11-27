
# Program Penentuan Nilai Mahasiswa
print('Masukkan nama anda:')
nama = input()

nilai = 80


if (nilai>79 and nilai<101):
    print(f"{nama} mendapatkan nilai A")
elif (nilai>65 and nilai<80):
    print(f"{nama} mendapatkan nilai B")
elif (nilai>50 and nilai<66):
    print(f"{nama} mendapatkan nilai C")
elif (nilai>0 and nilai<51):
    print(f"{nama} mendapatkan nilai D")
else:
    print("Nilai Invalid")