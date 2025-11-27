import math

def luas_kubus(sisi):
    return 6 * sisi * sisi

def luas_balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

def luas_bola(jari_jari):
    return 4 * math.pi * jari_jari * jari_jari

def luas_tabung(jari_jari, t):
    return 2 * math.pi * jari_jari * (jari_jari + t)

def luas_kerucut(jari_jari, selimut):
    return math.pi * jari_jari * (jari_jari + selimut)