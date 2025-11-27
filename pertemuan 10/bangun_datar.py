import math

def luas_persegi(sisi):
    return sisi * sisi

def luas_segitiga(alas, tinggi):
    return 0.5 * alas * tinggi

def luas_lingkaran(jari_jari):
    return math.pi * jari_jari * jari_jari

def luas_ketupat(diagonal1, diagonal2):
    return 0.5 * diagonal1 *  diagonal2

def luas_jajar_genjang(panjang, lebar):
    return panjang * lebar