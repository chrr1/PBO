class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_mahasiswa(self):
        print(f"Nama: {self.nama}")


class MahasiswaRPL:
    def belajar_rpl(self):
        print("Belajar PBO")


class MahasiswaAktif(Mahasiswa, MahasiswaRPL):
    def status(self):
        print("Status: Mahasiswa Aktif")


mhs = MahasiswaAktif("Adik Christian")

mhs.tampilkan_mahasiswa()
mhs.belajar_rpl()
mhs.status()