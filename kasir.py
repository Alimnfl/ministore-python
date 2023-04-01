total = 0
barang = []
harga = []

while True: 
    print("""Daftar Barang \n
1. Roti \t 6000
2. Es Krim \t 10000
3. Coklat \t 12000
4. Buku \t 10000
5. Penghapus \t 3000
6. Pensil \t 3000
7. Kantong Plastik \t 15000
8. Penggaris \t 8000
9. Kaca \t 30000
10. Goriorio \t 8000
11. Bengbeng \t 2000
12. Malkist Kelapa \t 3000
13. Recheese Keju \t 2000
14. Recheese Coklat \t 2000
15. Larutan Cap BADAK \t 9000
""")

    try:
        kode = int(input("Masukkan kode barang : "))
        if kode == 1:
            barang.append('Roti')
            harga.append(5000)
            total += 5000
        elif kode == 2:
            barang.append('Es Krim')
            harga.append(10000)
            total += 10000
        elif kode == 3:
            barang.append('Coklat')
            harga.append(12000)
            total += 12000
        elif kode == 4:
            barang.append('Buku')
            harga.append(10000)
            total += 10000
        elif kode == 5:
            barang.append('Penghapus')
            harga.append(3000)
            total += 3000
        elif kode == 6:
            barang.append('Pensil')
            harga.append(3000)
            total += 3000
        elif kode == 7:
            barang.append('Kantong Plastik')
            harga.append(15000)
            total += 15000
        elif kode == 8:
            barang.append('Penggaris')
            harga.append(8000)
            total += 8000
        elif kode == 9:
            barang.append('Kaca')
            harga.append(30000)
            total += 30000
        elif kode == 10:
            barang.append('Goriorio')
            harga.append(8000)
            total += 8000
        elif kode == 11:
            barang.append('Bengbeng')
            harga.append(2000)
            total += 2000
        elif kode == 12:
            barang.append('Malkist Kelapa')
            harga.append(3000)
            total += 3000
        elif kode == 13:
            barang.append('Recheese Keju')
            harga.append(2000)
            total += 2000
        elif kode == 14:
            barang.append('Recheese Coklat')
            harga.append(2000)
            total += 2000
        elif kode == 15:
            barang.append('Larutan Cap Badak')
            harga.append(9000)
            total += 9000
        else:
            print("Barang tidak ada dalam list")

    except ValueError:
        print("Kode tidak valid");

    lanjut = input('lanjut belanja? (y/t) : ')
    if lanjut == 't':
        print(" ")
        break

print('Barang yang dibeli : ', barang)
print('Harga barangnya : ', harga)
print('Total yang harus dibayar : ', total, '\n')

uang = int(input('Masukkan uang pembayaran : '))
if uang > total:
    print('Kembaliannya : ', uang - total)
elif uang == total:
    print('Uang pas, YEAY!!')
else:
    print('Uangnya kurang bro...', uang-total)