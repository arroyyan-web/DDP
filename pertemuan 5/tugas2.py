print("Program Menghitung Luas Bangun Datar")
print("1. Persegi")
print("2. Lingkaran")
print("3. Segitiga")

hitung = int(input("Memlih Program (1/2/3): "))

match hitung:
    case 1:
        sisi = float(input("Masukan Panjang Sisi"))
        luas = sisi * sisi
        print(luas)
    case 2: 
        r = float(input("Masukan jari-jari Lingkaran"))
        luas = 3.14 * r * r
        print(luas)
    case 3: 
        alas = float(input("Masukan Alas Segitiga"))
        tinggi = float(input("Masukan Tinggi Segitiga"))
        luas = 0.5 * alas * tinggi
        print(luas)
    case _: 
        print("SALAH PILIH")