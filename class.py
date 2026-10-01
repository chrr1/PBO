class Laptop:
    def __init__(self, warna, merek, processor):
        self.warna = warna
        self.merek = merek
        self.processor = processor
        self.ram = 8

    def tambah_ram(self):
        self.ram += 8 


laptop_1 = Laptop("Hitam", "Asus", "Intel")

print("Sebelum ditambahkan: ")
print(laptop_1.ram)

laptop_1.tambah_ram()

print("Setelah ditambahkan: ")
print(laptop_1.ram)