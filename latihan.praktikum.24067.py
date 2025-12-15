def hitung_diskon(harga, persen_diskon):
    total = harga - (harga * persen_diskon / 100)
    return total

print("Harga setelah diskon:", hitung_diskon(100000, 20))
