print("-" * 25)
class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

    def info(self):
        print("Merk kendaraan:", self.merk)

class Motor(Kendaraan):
    def jalan(self):
        print("Motor Baru")

class Kendaraan:
    def __init__(self, merk):
        self.merk = merk

class motor(Kendaraan):
    def __init__(self, merk, warna):
        super().__init__(merk)
        self.warna = warna

m = Motor("Honda Genio")
m.info()
m.jalan()
a = motor("Honda Genio", "Hitam")
print(a.merk)
print(a.warna)
print("-" * 25)