import bangun_datar, bangun_ruang

# luas_bangun_datar
print("====Luas Bangun Datar====")
print(f"Luas Persegi = {bangun_datar.luas_persegi(5)}")
print(f"Luas Segitiga = {bangun_datar.luas_segitiga(3, 5)}")
print(f"Luas Lingkaran = {bangun_datar.luas_lingkaran(1)}")
print(f"Luas Ketupat = {bangun_datar.luas_ketupat(10, 10)}")
print(f"Luas Jajar Genjang = {bangun_datar.luas_jajar_genjang(3, 4)}")

# luas_bangun_ruang
print("====Luas Bangun Ruang====")
print(f"Luas Kubus = {bangun_ruang.luas_kubus(5)}")
print(f"Luas Balok = {bangun_ruang.luas_balok(3, 5, 7)}")
print(f"Luas Bola = {bangun_ruang.luas_bola(1)}")
print(f"Luas Tabung = {bangun_ruang.luas_tabung(1, 10)}")
print(f"Luas Kerucut = {bangun_ruang.luas_kerucut(1, 4)}")